""" A utility module for the prefect_monte_carlo package. """

from uuid import UUID

from pycarlo.common.errors import GqlError

from prefect_monte_carlo.credentials import MonteCarloCredentials


async def rule_uuid_from_name(
    rule_name: str,
    monte_carlo_credentials: MonteCarloCredentials,
) -> UUID:
    """Helper function to get the UUID of a Monte Carlo SQL monitor rule by name."""
    query = f"""
        query {{
            getCustomRule (
                descriptionContains: "{rule_name}"
        ) {{ uuid }}
    }}
    """
    client = monte_carlo_credentials.get_client()
    return UUID(client(query).get_custom_rule.uuid)
