"""Module for GraphQL queries and mutations."""

from typing import Dict, Optional

from prefect import task

from prefect_monte_carlo.credentials import MonteCarloCredentials


@task
async def execute_graphql_query(
    montecarlo_credentials: MonteCarloCredentials,
    query: str,
    variables: Optional[Dict] = None,
) -> dict:
    """
    Executes a GraphQL query against the Monte Carlo GraphQL API.

    Args:
        montecarlo_credentials: credentials to authenticate with the
            Monte Carlo GraphQL API.
        query: the GraphQL query to execute.
        variables: the variables to pass to the GraphQL query.

    Returns:
        The results of the GraphQL query.

    Example:
        Executes a simple GraphQL query against the Monte Carlo GraphQL API.
        ```python
        from prefect import flow
        from prefect_monte_carlo import execute_graphql_query
        from prefect_monte_carlo.credentials import MonteCarloCredentials

        @flow
        def example_execute_query():
            montecarlo_credentials = MonteCarloCredentials.load(
                "my-montecarlo-credentials"
            )
            result = execute_graphql_query(
                montecarlo_credentials=montecarlo_credentials,
                query="query getUser { getUser { email firstName lastName }}",
            )

        example_execute_query()
        ```

        Executes a GraphQL query with variables.
        ```python
        from prefect import flow

        from prefect_monte_carlo.credentials import MonteCarloCredentials
        from prefect_monte_carlo.graphql import execute_graphql_query

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

            result = execute_graphql_query(
                montecarlo_credentials=mc_creds,
                query=query,
                variables={"first":10}
            )

        if __name__ == "__main__":
            test_mc()
        ```
    """
    client = await montecarlo_credentials.get_client()
    return client(query, variables=variables)
