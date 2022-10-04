from uuid import UUID

from prefect import flow

from prefect_monte_carlo.circuit_breakers import monitor_rule_breached
from prefect_monte_carlo.credentials import MonteCarloCredentials


async def test_circuit_breaker_with_uuid(monte_carlo_credentials):
    """Test that the circuit breaker task can be run with a rule UUID."""

    @flow
    def test(we_really_care_about_UUID: bool = False):
        # we can also pass both `rule_name` and `namespace` instead of rule_uuid
        rule_uuid = (
            UUID("af6fdb62-7496-4b8b-ba09-38f83a311c17")
            if we_really_care_about_UUID
            else "af6fdb62-7496-4b8b-ba09-38f83a311c17"  # just a str will do
        )
        return monitor_rule_breached(
            monte_carlo_credentials=MonteCarloCredentials.load(
                "monte-carlo-credentials"
            ),
            rule_uuid=rule_uuid,
        )

    result = test()

    assert isinstance(result, bool)


# if __name__ == "__main__":
#     @circuit_breaker(
#         rule_uuid="af6fdb62-7496-4b8b-ba09-38f83a311c17",
#         monte_carlo_credentials=MonteCarloCredentials.load("monte-carlo-credentials")
#     )
#     @flow
#     def only_run_if_not_breached(shabba = "ranks"):
#         logger = get_run_logger()
#         logger.info(f"shabba {shabba}")

#     only_run_if_not_breached()
