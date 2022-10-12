""" Module defining tasks for interacting with Monte Carlo resources. """

import box
from prefect import task

from prefect_monte_carlo.credentials import MonteCarloCredentials


@task
async def get_monte_carlo_resources(
    monte_carlo_credentials: MonteCarloCredentials,
) -> box.BoxList:
    """
    Task to retrieve all Monte Carlo resources.

    Args:
        monte_carlo_credentials: The Monte Carlo credentials block used to generate
            an authenticated GraphQL API client via pycarlo.
    Returns:
        A `box.BoxList` of all Monte Carlo resources.
    """

    client = monte_carlo_credentials.get_client()
    query = """
        query {
            getResources {
                name
                type
                id
                uuid
                isDefault
                isUserProvided
            }
        }
    """
    return client(query)
