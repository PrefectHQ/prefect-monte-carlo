from box import BoxList
from prefect import flow

from prefect_monte_carlo.resources import get_monte_carlo_resources


async def test_get_monte_carlo_resources(
    monte_carlo_creds, mock_monte_carlo_resources, mock_monte_carlo_resources_response
):
    @flow
    async def test_flow():
        return await get_monte_carlo_resources(monte_carlo_creds)

    resources = await test_flow()

    assert isinstance(resources, BoxList)
    assert resources == mock_monte_carlo_resources
