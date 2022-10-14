"""Module to define Monte Carlo utility functions."""

from typing import Dict, List
from uuid import UUID

from prefect_monte_carlo.credentials import MonteCarloCredentials
from prefect_monte_carlo.exceptions import MonteCarloIncorrectTagsFormatException


async def rule_uuid_from_name(
    rule_name: str,
    monte_carlo_credentials: MonteCarloCredentials,
) -> UUID:
    """Get the UUID of a Monte Carlo monitor rule from its name.


    Args:
        rule_name: Name of the Monte Carlo monitor rule.
        monte_carlo_credentials: Credentials
            to authenticate with the Monte Carlo GraphQL API.
    """
    query = f"""
        query {{
            getCustomRule (
                descriptionContains: "{rule_name}"
        ) {{ uuid }}
    }}
    """
    client = monte_carlo_credentials.get_client()
    return client(query).get_custom_rule.uuid


def validate_tags(tags: List[Dict[str, str]]):
    """Validate that Monte Carlo lineage node tags are in the correct format.

    Args:
        tags: List of user-defined tags to validate.

    Raises:
        MonteCarloIncorrectTagsFormatException: If the tags are not well-formatted.

    """
    for tag in tags:
        if tag.keys() != {"propertyName", "propertyValue"}:
            raise MonteCarloIncorrectTagsFormatException(
                "Must provide tags as a list of dicts like "
                '[{"propertyName": "tag_name", "propertyValue": "tag_value"}].',
                "You provided: ",
                tag,
            )
