""" Module for interacting with Monte Carlo circuit breakers / monitor rules. """
import functools
from typing import Optional
from uuid import UUID

from prefect import get_run_logger, task
from prefect.states import Cancelled
from prefect.utilities.asyncutils import is_async_fn
from pycarlo.features.circuit_breakers import CircuitBreakerService
from pycarlo.features.circuit_breakers.exceptions import CircuitBreakerPollException

from prefect_monte_carlo.credentials import MonteCarloCredentials
from prefect_monte_carlo.utilities import rule_uuid_from_name


def skip_if_circuit_breaker_flipped(
    monte_carlo_credentials: MonteCarloCredentials,
    rule_uuid: Optional[UUID] = None,
    rule_name: Optional[str] = None,
):
    """Decorator to run a user-defined flow only if a given Monte Carlo
    monitor rule is not breached.

    This decorator must be placed between your `@flow` decorator and
    the python function that defines your flow.

    Args:
        monte_carlo_credentials: The credentials to use to generate an
            authenticated Monte Carlo GraphQL client via PyCarlo.
        rule_uuid: The UUID of the monitor rule to check.
        rule_name: The name of the monitor rule to check.

    Examples:
        Define a flow that will only run if `my_monitor_rule` is not breached:
        ```python
        from prefect import flow
        from prefect_monte_carlo.circuit_breakers import skip_if_circuit_breaker_flipped
        from prefect_monte_carlo.credentials import MonteCarloCredentials

        # suppose `my_monitor_rule` has a UUID `1123e4567-e89b-12d3-a456-426614174000`

        @flow
        @skip_if_circuit_breaker_flipped(
            rule_uuid="123e4567-e89b-12d3-a456-426614174000",
            monte_carlo_credentials=MonteCarloCredentials.load("my-montecarlo-credentials")
        )
        def my_flow():
            print("I will only print if `my_monitor_rule` is not breached.")
        ```

        Reference a rule by name:
        ```python
        @flow
        @skip_if_circuit_breaker_flipped(
            rule_name="my_monitor_rule",
            monte_carlo_credentials=MonteCarloCredentials.load("my-montecarlo-credentials")
        )
        def my_flow():
            print("I will only print if `my_monitor_rule` is not breached.")
        ```
    """
    monitor_rule_kwargs = dict(
        rule_name=rule_name,
        rule_uuid=rule_uuid,
        monte_carlo_credentials=monte_carlo_credentials,
    )

    def decorator(func):
        """Layer to catch the function being decorated."""

        if not is_async_fn(func):

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                """Modified synchronous user-flow to return."""
                if circuit_breaker_is_flipped(**monitor_rule_kwargs):
                    return Cancelled()
                return func(*args, **kwargs)

            return wrapper
        else:

            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                """Modified asynchronous user-flow to return."""
                if circuit_breaker_is_flipped(**monitor_rule_kwargs):
                    return Cancelled()
                return await func(*args, **kwargs)

            return wrapper

    return decorator


@task
async def circuit_breaker_is_flipped(
    monte_carlo_credentials: MonteCarloCredentials,
    rule_uuid: Optional[UUID] = None,
    rule_name: Optional[str] = None,
    timeout_in_minutes: Optional[int] = 5,
) -> bool:
    """A task to check if a Monte Carlo circuit breaker / monitor rule is breached.

    If `rule_name` is provided, the task will attempt to fetch the associated
    `rule_uuid` from the Monte Carlo GraphQL API and use it to trigger the custom
    rule.

    To surface pycarlo `CircuitBreakerService` polling logs as Prefect logs, use the
    `DEBUG` log level when running your flow.

    Args:
        monte_carlo_credentials: The Monte Carlo credentials block used to
            generate an authenticated GraphQL API client.
        rule_uuid: UUID of the rule (custom SQL monitor) to execute.
        rule_name: Name of the rule (custom SQL monitor) to execute.
        timeout_in_minutes: How long to wait for SQL rule run logs.

    Raises:
        ValueError: If both (or neither) `rule_uuid` and `rule_name` are provided.

    Returns:
        `True` if the rule is breached, `False` otherwise.

    Example:
        Check if a rule is breached by UUID:
        ```python
        from prefect import flow
        from prefect.orion.schemas.states import Cancelled
        from prefect_monte_carlo.circuit_breakers import circuit_breaker_is_flipped

        @task
        def do_something_if_not_breached():
            pass

        @flow
        def conditional_flow():
            # we can also pass `rule_name` instead of rule_uuid
            rule_uuid = "af6fdb62-7496-4b8b-ba09-38f83a311c17" # or as a UUID object
            if circuit_breaker_is_flipped(
                monte_carlo_credentials=MonteCarloCredentials.load(
                    "monte-carlo-credentials"
                ),
                rule_uuid=rule_uuid
            ):
                return Cancelled(message="Monitor rule breached - cancelling flow run.")

            do_something_if_not_breached()
        ```
    """
    monte_carlo_client = monte_carlo_credentials.get_client()

    if not (bool(rule_uuid) ^ bool(rule_name)):
        raise ValueError(
            "Please provide either `rule_uuid` or `rule_name`, but not both"
        )

    if rule_uuid:
        rule_uuid = UUID(rule_uuid)
    else:
        rule_uuid = await rule_uuid_from_name(
            rule_name=rule_name,
            monte_carlo_credentials=monte_carlo_credentials,
        )

    logger = get_run_logger()

    circuit_breaker_service = CircuitBreakerService(
        mc_client=monte_carlo_client, print_func=logger.debug
    )

    job_execution_uuid = circuit_breaker_service.trigger(rule_uuid=rule_uuid)

    logger.debug(
        f"Triggered rule: {rule_uuid} with job execution UUID: {job_execution_uuid}"
    )

    try:
        breaches_count = circuit_breaker_service.poll(
            job_execution_uuid=job_execution_uuid, timeout_in_minutes=timeout_in_minutes
        )

        if breaches_count > 0:
            logger.info(
                f"Found {breaches_count} breach(es)"
                f" for rule {rule_uuid} during job: {job_execution_uuid}"
                f" - see more details at https://getmontecarlo.com/monitors/{rule_uuid}"
            )
            return True

        logger.info(f"Found no breach for rule with uuid: '{rule_uuid}'.")
        return False

    except CircuitBreakerPollException as e:
        logger.error(
            f"Encountered an error when attempting to get circuit breaker status: {e!r}"
        )
        raise
