from prefect import task
from prefect_montecarlo.credentials import MontecarloCredentials
from typing import Dict, Optional

@task
async def execute_graphql_query(
    montecarlo_credentials: MontecarloCredentials,
    query: str,
    variables: Optional[Dict] = None,
) -> dict:
    """
    Executes a GraphQL query against the Montecarlo GraphQL API.

    Args:
        montecarlo_credentials: the credentials to authenticate with the Montecarlo GraphQL API.
        query: the GraphQL query to execute.
        variables: the variables to pass to the GraphQL query.

    Returns:
        The results of the GraphQL query.

    Example:
        Executes a simple GraphQL query against the Montecarlo GraphQL API.
        ```python
        from prefect import flow
        from prefect_montecarlo import execute_graphql_query
        from prefect_montecarlo.credentials import MontecarloCredentials

        @flow
        def example_execute_query():
            montecarlo_credentials = MontecarloCredentials.load(
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

        from prefect_montecarlo.credentials import MontecarloCredentials
        from prefect_montecarlo.graphql import execute_graphql_query

        mc_creds = MontecarloCredentials.load("monte-carlo-credentials")

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