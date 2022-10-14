import pytest

from prefect_monte_carlo.exceptions import MonteCarloIncorrectTagsFormatException
from prefect_monte_carlo.lineage import create_or_update_lineage


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
