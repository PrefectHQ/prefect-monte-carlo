import pytest
from box import BoxList
from prefect import flow
from pycarlo.common.errors import GqlError

from prefect_monte_carlo.graphql import (
    execute_graphql_operation,
    get_monte_carlo_resources,
)


async def test_execute_graphql_op_no_vars(
    monte_carlo_creds,
    sample_get_tables_query_response,
    mock_successful_get_tables_query_response,
):
    test_query = "query getTables { getTables { edges { node { fullTableId } } } }"

    @flow
    async def test_flow():
        return await execute_graphql_operation(
            monte_carlo_credentials=monte_carlo_creds,
            operation=test_query,
        )

    result = await test_flow()

    assert result == sample_get_tables_query_response


@pytest.mark.parametrize("variables", [{"second": 10}, None])
async def test_execute_graphql_op_with_bad_vars(
    monte_carlo_creds, variables, mock_bad_operation_response
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
        return await execute_graphql_operation(
            monte_carlo_credentials=monte_carlo_creds,
            operation=query,
            variables=variables,
        )

    with pytest.raises(GqlError):
        await test_flow()


async def test_get_monte_carlo_resources(
    monte_carlo_creds, mock_monte_carlo_resources, mock_monte_carlo_resources_response
):
    @flow
    async def test_flow():
        return await get_monte_carlo_resources(monte_carlo_creds)

    resources = await test_flow()

    assert isinstance(resources, BoxList)
    assert resources == mock_monte_carlo_resources
