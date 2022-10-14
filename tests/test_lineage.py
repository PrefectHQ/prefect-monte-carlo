import pytest
from prefect import flow

from prefect_monte_carlo.exceptions import MonteCarloIncorrectTagsFormatException
from prefect_monte_carlo.lineage import (
    MonteCarloLineageNode,
    create_or_update_lineage,
    create_or_update_lineage_edge,
    create_or_update_lineage_node,
)


async def test_create_or_update_lineage(
    mock_source_dict,
    mock_destination_dict,
    monte_carlo_creds,
    mock_create_or_update_lineage_node,
    mock_create_or_update_lineage_edge,
):

    edge_id = await create_or_update_lineage(
        monte_carlo_credentials=monte_carlo_creds,
        source=mock_source_dict,
        destination=mock_destination_dict,
    )

    assert isinstance(edge_id, str)


async def test_create_or_update_lineage_source_with_bad_tags(
    mock_destination_dict, monte_carlo_creds
):

    source_with_bad_tags = dict(
        node_name="source_dataset",
        object_id="source_dataset",
        resource_name="blah",
        tags=[{"non": "conforming", "tag": "structure"}],
    )
    with pytest.raises(MonteCarloIncorrectTagsFormatException):
        await create_or_update_lineage(
            monte_carlo_credentials=monte_carlo_creds,
            source=source_with_bad_tags,
            destination=mock_destination_dict,
        )


async def test_create_or_update_lineage_destination_with_bad_tags(
    mock_source_dict, monte_carlo_creds
):

    destination_with_bad_tags = dict(
        node_name="destination_dataset",
        object_id="destination_dataset",
        resource_name="blah",
        tags=[{"non": "conforming", "tag": "structure"}],
    )
    with pytest.raises(MonteCarloIncorrectTagsFormatException):
        await create_or_update_lineage(
            monte_carlo_credentials=monte_carlo_creds,
            source=mock_source_dict,
            destination=destination_with_bad_tags,
        )


async def test_create_or_update_lineage_node_using_kwargs(
    monte_carlo_creds, mock_create_or_update_lineage_node_response
):
    @flow
    async def test_flow():

        return await create_or_update_lineage_node(
            monte_carlo_credentials=monte_carlo_creds,
            node_name="test_node",
            object_id="test_object_id",
            object_type="table",
            resource_name="test_resource_name",
        )

    node_mcon = await test_flow()

    assert node_mcon == "MCON++someid++table++source_raw_customer"


async def test_create_or_update_lineage_node_using_model(
    monte_carlo_creds, mock_create_or_update_lineage_node_response
):
    node_model = MonteCarloLineageNode(
        node_name="source_dataset",
        object_id="source_dataset",
        object_type="table",
        resource_name="ecommerce_system",
        tags=[{"propertyName": "dataset_owner", "propertyValue": "some_team"}],
    )

    @flow
    async def test_flow():

        return await create_or_update_lineage_node(
            monte_carlo_credentials=monte_carlo_creds, **node_model.dict()
        )

    node_mcon = await test_flow()

    assert node_mcon == "MCON++someid++table++source_raw_customer"


async def test_create_or_update_lineage_edge_using_kwargs(
    monte_carlo_creds,
    mock_create_or_update_lineage_edge_response,
    mock_source_dict,
    mock_destination_dict,
):
    @flow
    async def test_flow():
        return await create_or_update_lineage_edge(
            monte_carlo_credentials=monte_carlo_creds,
            source=mock_source_dict,
            destination=mock_destination_dict,
        )

    edge_id = await test_flow()

    assert edge_id == "e3546a7dc6ee45f0eb63fda79dbc5de4994ffe2471c136aa057b95d3f9e5bd2e"