""" Module for interacting with Monte Carlo circuit breakers / SQL monitor rules. """
import functools
from typing import Optional
from uuid import UUID

from prefect import get_run_logger, task
from prefect.orion.schemas.states import Cancelled
from prefect.utilities.asyncutils import is_async_fn
from pycarlo.features.circuit_breakers import CircuitBreakerService
from pycarlo.features.circuit_breakers.exceptions import CircuitBreakerPollException

from prefect_monte_carlo.credentials import MonteCarloCredentials
from prefect_monte_carlo.utililties import rule_uuid_from_name


def skip_if_circuit_breaker_flipped(**monitor_rule_kwargs):
    """Decorator to run a user-defined flow only if a given Monte Carlo
    SQL monitor rule is not breached."""

    def decorator(func):
        """Layer to catch the function being decorated."""

        if not is_async_fn(func):

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                """Modified synchronous user-flow to return."""
                if is_monitor_rule_breached(**monitor_rule_kwargs):
                    return Cancelled()
                return func(*args, **kwargs)

            return wrapper
        else:

            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                """Modified asynchronous user-flow to return."""
                if is_monitor_rule_breached(**monitor_rule_kwargs):
                    return Cancelled()
                return await func(*args, **kwargs)

            return wrapper

    return decorator


@task
async def is_monitor_rule_breached(
    monte_carlo_credentials: MonteCarloCredentials,
    rule_uuid: Optional[UUID] = None,
    rule_name: Optional[str] = None,
    timeout_in_minutes: Optional[int] = 5,
) -> bool:
    """A task to check if a Monte Carlo circuit breaker / sql monitor rule is breached.

    Args:
        monte_carlo_credentials: The Monte Carlo credentials block used to
            generate an authenticated GraphQL API client.
        rule_uuid: UUID of the rule (custom SQL monitor) to execute.
        rule_name: Name of the rule (custom SQL monitor) to execute.
        timeout_in_minutes: How long to wait for SQL rule run logs.

    Raises:
        ValueError: If an incorrect combination of rule references is passed.

    Examples:
        - Check if a rule is breached by UUID:
        ```python
        from prefect import flow
        from prefect.orion.schemas.states import Cancelled
        from prefect_monte_carlo import monitor_rule_breached

        @task
        def do_something_if_not_breached():
            pass

        @flow
        def test(we_really_care_about_UUID: bool = False):
            # we can also pass `rule_name` instead of rule_uuid
            rule_uuid = "af6fdb62-7496-4b8b-ba09-38f83a311c17" # or as a UUID
            if monitor_rule_breached(
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

    if not (rule_uuid or rule_name):
        raise ValueError("Must pass either `rule_uuid` OR `rule_name`")

    if rule_uuid:
        try:
            rule_uuid = UUID(rule_uuid)
        except ValueError:
            raise

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
        N_breaches = circuit_breaker_service.poll(
            job_execution_uuid=job_execution_uuid, timeout_in_minutes=timeout_in_minutes
        )

        if N_breaches > 0:
            logger.info(
                f"Found {N_breaches} breach(es) of rule via job '{job_execution_uuid}'"
                f" - see more details at https://getmontecarlo.com/monitors/{rule_uuid}"
            )
            return True

        logger.info(f"Found no breach for rule with uuid: '{rule_uuid}'.")
        return False

    except CircuitBreakerPollException as e:
        logger.error(f"{e!r}")
        raise
