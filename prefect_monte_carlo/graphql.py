"""Module for GraphQL queries and mutations."""

from typing import Any, Dict, List, Optional
from uuid import UUID

from box import Box, BoxList
from prefect import task
from pycarlo.common.errors import GqlError

from prefect_monte_carlo.credentials import MonteCarloCredentials


@task
async def get_resources(monte_carlo_credentials: MonteCarloCredentials) -> BoxList:
    """Task to retrieve all Monte Carlo resources.

    Args:
        monte_carlo_credentials: The Monte Carlo credentials block used to generate
            an authenticated GraphQL API client via pycarlo.

    Returns:
        A `BoxList` of all Monte Carlo resources.
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
    return client(query).get_resources


@task
async def execute_graphql_operation(
    monte_carlo_credentials: MonteCarloCredentials,
    operation: str,
    variables: Optional[Dict] = None,
) -> Box:
    """
    Executes a GraphQL operation via the Monte Carlo GraphQL API.

    Args:
        montecarlo_credentials: Credentials to authenticate with the
            Monte Carlo GraphQL API.
        operation: The GraphQL operation to execute - it can be a valid GraphQL
            query or mutation.
        variables: The variables to pass to the GraphQL operation.

    Returns:
        The results of the GraphQL operation as a Box object. See
        [the python-box docs](https://pypi.org/project/python-box/).

    Example:
        Executes a simple GraphQL query against the Monte Carlo GraphQL API.
        ```python
        from prefect import flow
        from prefect_monte_carlo import execute_graphql_operation
        from prefect_monte_carlo.credentials import MonteCarloCredentials

        @flow
        def example_execute_query():
            montecarlo_credentials = MonteCarloCredentials.load(
                "my-montecarlo-credentials"
            )
            result = execute_graphql_operation(
                montecarlo_credentials=montecarlo_credentials,
                operation="query getUser { getUser { email firstName lastName }}",
            )

        example_execute_query()
        ```

        Executes a GraphQL query with variables.
        ```python
        from prefect import flow

        from prefect_monte_carlo.credentials import MonteCarloCredentials
        from prefect_monte_carlo.graphql import execute_graphql_operation

        mc_creds = MonteCarloCredentials.load("monte-carlo-credentials")

        query = '''
            query getTables($first: Int){
                getTables(first: $first) {
                    edges {
                        node {
                            fullTableId
                        }
                    }
                }
            }
        '''

        @flow
        def test_mc():

            result = execute_graphql_operation(
                montecarlo_credentials=mc_creds,
                operation=query,
                variables={"first":10}
            )

        if __name__ == "__main__":
            test_mc()
        ```
    """
    client = monte_carlo_credentials.get_client()
    return client(operation, variables=variables)
