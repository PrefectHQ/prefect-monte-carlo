""" Module for interacting with Monte Carlo circuit breakers / SQL monitor rules. """
from typing import Optional
from uuid import UUID

from prefect import flow, get_run_logger, task
from prefect.orion.schemas.states import Completed
from pycarlo.features.circuit_breakers import CircuitBreakerService
from pycarlo.features.circuit_breakers.exceptions import CircuitBreakerPollException

from prefect_monte_carlo.credentials import MonteCarloCredentials


def circuit_breaker(**monitor_rule_kwargs):
    """Decorator to run a parent flow whose children are only
    run if a Monte Carlo SQL monitor rule is not breached."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            @flow
            def circuit_breaker_flow(**monitor_rule_kwargs):
                if monitor_rule_breached(**monitor_rule_kwargs):
                    return Completed(
                        message=f"Circuit breaker tripped for rule: {dict(**monitor_rule_kwargs)}."
                    )
                func(*args, **kwargs)

            return circuit_breaker_flow(**monitor_rule_kwargs)

        return wrapper

    return decorator


@task
def monitor_rule_breached(
    monte_carlo_credentials: MonteCarloCredentials,
    rule_uuid: Optional[UUID] = None,
    rule_name: Optional[str] = None,
    namespace: Optional[str] = None,
    timeout_in_minutes: Optional[int] = 5,
) -> bool:
    """A task to check if a Monte Carlo circuit breaker / sql monitor rule is breached.

    Args:
        monte_carlo_credentials: The Monte Carlo credentials block used to
            generate an authenticated GraphQL API client.
        rule_uuid: UUID of the rule (custom SQL monitor) to execute.
        rule_name: Name of the rule (custom SQL monitor) to execute.
        namespace: Namespace of the rule (custom SQL monitor) to execute.
        timeout_in_minutes: How long to wait for SQL rule run logs.

    Raises:
        ValueError: If an incorrect combination of rule references is passed.

    Examples:
        - Check if a rule is breached by UUID:
        ```python
        from prefect import flow
        from prefect_monte_carlo import monitor_rule_breached

        @task
        def do_something_if_not_breached():
            pass

        @flow
        def test(we_really_care_about_UUID: bool = False):
            # we can also pass `rule_name` and `namespace` instead of rule_uuid
            rule_uuid = (
                UUID("af6fdb62-7496-4b8b-ba09-38f83a311c17") if we_really_care_about_UUID
                else "af6fdb62-7496-4b8b-ba09-38f83a311c17" # just a str will do
            )
            if monitor_rule_breached(
                monte_carlo_credentials=MonteCarloCredentials.load(
                    "monte-carlo-credentials"
                ),
                rule_uuid=rule_uuid
            ):
                return Completed(message="SQL Monitor rule breached - skipping flow run.")

            do_something_if_not_breached()
            ```
    """
    monte_carlo_client = monte_carlo_credentials.get_client()

    valid_rule_reference_passed = rule_uuid or (rule_name and namespace)
    all_passed = all([rule_uuid, rule_name, namespace])

    if not valid_rule_reference_passed or all_passed:
        raise ValueError("Must pass either `rule_uuid` OR `rule_name` and `namespace`.")

    if rule_uuid:
        circuit_breaker_svc_kwargs = dict(rule_uuid=rule_uuid)
    else:
        circuit_breaker_svc_kwargs = dict(rule_name=rule_name, namespace=namespace)

    logger = get_run_logger()

    circuit_breaker_service = CircuitBreakerService(
        mc_client=monte_carlo_client, print_func=logger.info
    )

    job_execution_uuid = circuit_breaker_service.trigger(**circuit_breaker_svc_kwargs)

    logger.debug(
        f"Triggered rule: {rule_uuid} with job execution UUID: {job_execution_uuid}"
    )

    try:
        N_breaches = circuit_breaker_service.poll(
            job_execution_uuid=job_execution_uuid, timeout_in_minutes=timeout_in_minutes
        )

        if N_breaches > 0:
            logger.info(f"Found {N_breaches} breach(es) of this rule.")
            return True

        logger.info("Found no breaches of rule.")
        return False

    except CircuitBreakerPollException as e:
        logger.error(f"{e!r}")
        raise
