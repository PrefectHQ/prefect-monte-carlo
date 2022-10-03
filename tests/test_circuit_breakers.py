from uuid import UUID

from prefect import flow

from prefect_monte_carlo.circuit_breakers import circuit_breaker
from prefect_monte_carlo.credentials import MonteCarloCredentials


async def test_circuit_breaker_with_uuid(monte_carlo_credentials):
    """Test that the circuit breaker task can be run with a rule UUID."""

    @flow
    def test():
        rule_uuid = UUID("af6fdb62-7496-4b8b-ba09-38f83a311c17")

        return circuit_breaker(
            monte_carlo_credentials=MonteCarloCredentials.load(
                "monte-carlo-credentials"
            ),
            rule_uuid=rule_uuid,
        )

    result = test()

    assert isinstance(result, bool)
