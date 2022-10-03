""" Module for interacting with Monte Carlo circuit breakers / SQL monitor rules. """

from typing import Optional
from uuid import UUID

from prefect import get_run_logger, task
from pycarlo.features.circuit_breakers import CircuitBreakerService

from prefect_monte_carlo.credentials import MonteCarloCredentials


@task
async def circuit_breaker(
    monte_carlo_credentials: MonteCarloCredentials,
    rule_uuid: Optional[UUID] = None,
    rule_name: Optional[str] = None,
    namespace: Optional[str] = None,
) -> bool:
    """_summary_

    Args:
        monte_carlo_credentials: The Monte Carlo credentials block used to
            generate an authenticated GraphQL API client.
        rule_uuid: UUID of the rule (custom SQL monitor) to execute.
        rule_name: name of the rule (custom SQL monitor) to execute.
        namespace: Namespace of the rule (custom SQL monitor) to execute.

    Raises:
        ValueError: If an incorrect combination of rule references is passed.
    """
    monte_carlo_client = monte_carlo_credentials.get_client()

    valid_rule_reference_passed = rule_uuid or (rule_name and namespace)
    all_passed = all([rule_uuid, rule_name, namespace])

    if not valid_rule_reference_passed or all_passed:
        raise ValueError("Must pass either `rule_uuid` OR `rule_name` and `namespace`.")

    if rule_uuid:
        rule_reference = dict(rule_uuid=rule_uuid)
    else:
        rule_reference = dict(rule_name=rule_name, namespace=namespace)

    logger = get_run_logger()

    circuit_breaker = CircuitBreakerService(
        mc_client=monte_carlo_client, print_func=logger.info
    )

    if circuit_breaker.trigger_and_poll(**rule_reference):
        logger.info("Circuit breaker triggered")
