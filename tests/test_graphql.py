import pytest

from prefect import flow
from prefect_montecarlo.graphql import execute_graphql_query
from pycarlo.common.errors import GqlError

async def test_execute_graphql_query_no_vars(
    montecarlo_credentials,
    sample_get_tables_query_response,
    mock_successful_get_tables_query_response
):
    @flow
    async def test_flow():
        return await execute_graphql_query(
            montecarlo_credentials=montecarlo_credentials,
            query="query getTables { getTables { edges { node { fullTableId } } } }",
        )
        
    result = await test_flow()
    
    assert result == sample_get_tables_query_response

@pytest.mark.parametrize("variables", [{"second": 10}, None])
async def test_execute_graphql_query_with_bad_vars(
    montecarlo_credentials,
    variables,
    mock_bad_variable_get_tables_query_response
):
    @flow
    async def test_flow():
        query = """
            query getTables($first: Int){
                getTables(first: $first) {
                    edges {
                        node {
                            fullTableId
                        }
                    }
                }
            }
        """
        return await execute_graphql_query(
            montecarlo_credentials=montecarlo_credentials,
            query=query,
            variables=variables
        )
        
    with pytest.raises(GqlError):
        await test_flow()
    
