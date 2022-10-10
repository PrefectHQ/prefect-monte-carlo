""" Module to defines tasks interacting with Monte Carlo lineage resources. """

from datetime import datetime, timedelta
from typing import Any, Dict, Optional, Union

import box
from prefect import task

from prefect_monte_carlo.credentials import MonteCarloCredentials


@task
def create_or_update_lineage(
    source: Dict[str, Any],
    destination: Dict[str, Any],
    monte_carlo_credentials: MonteCarloCredentials,
    expire_at: Optional[str] = None,
) -> box.BoxList:
    """Task for creating or updating a lineage node for the given source
    and destination nodes, as well as for creating a lineage edge between those nodes.

    Args:
        source: A source node configuration - expected to include the following
            keys: `node_name`, `object_id`, `object_type`, `resource_name`.
        destination: A destination node configuration - expected to include the
            following keys: `node_name`, `object_id`, `object_type`, `resource_name`,
            and optionally also a list of `tags`.
        monte_carlo_credentials: The Monte Carlo credentials block used to generate
            an authenticated GraphQL API client via pycarlo.
        expire_at: Date and time indicating when to expire
            a source-destination edge.

    Raises:
        ValueError: _description_

    Returns:
        box.BoxList: _description_
    """
    if not (source.get("object_type") and destination.get("object_type")):
        raise ValueError(
            "Source and destination objects must have an `object_type` field."
        )


@task
def create_or_update_node_with_tags() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    pass


@task
def create_or_update_lineage_edge(
    source: Dict[str, Any],
    destination: Dict[str, Any],
    monte_carlo_credentials: MonteCarloCredentials,
    expire_at: Optional[Union[datetime, str]] = None,
) -> box.Box:
    """Create or update a Monte Carlo lineage edge via the GraphQL API.

    Args:
        source: The source node of the lineage edge.
        destination: The destination node of the lineage edge.
        monte_carlo_credentials: The Monte Carlo credentials block used to generate
            an authenticated GraphQL API client via pycarlo.
        expire_at: The time at which the lineage edge should expire. If not provided,
            the lineage edge will expire after 1 day.

    Returns:
        The `edgeId` of the created or updated lineage edge.

    Example:
        Create a lineage edge between a source table and a destination table:
        ```python
        from prefect import flow
        from prefect_monte_carlo.credentials import MonteCarloCredentials
        from prefect_monte_carlo.lineage import create_or_update_lineage_edge

        source = dict(
            node_name="example_table_name",
            object_id="example_table_name",
            # "table" is recommended, but you can use any string, e.g. "csv_file"
            object_type="table",
            resource_name="name_your_source_system",
            tags=[{"propertyName": "key", "propertyValue": "value"}]
        )

        destination = dict(
            node_name="db_name:schema_name.table_name",
            object_id="db_name:schema_name.table_name",
            object_type="table",
            resource_name="your_dwh_resource_name",
            tags=[{"propertyName": "key", "propertyValue": "value"}]
        )

        @flow
        def my_monte_carlo_flow():
            create_or_update_lineage_edge(
                source={},
                destination={},
                monte_carlo_credentials=MonteCarloCredentials.load("my-mc-creds"),
                expire_at=datetime.now() + timedelta(days=10),
            )
        ```

    """
    if expire_at:
        expire_at = (
            expire_at.isoformat() if isinstance(expire_at, datetime) else expire_at
        )
    else:
        expire_at = (datetime.now() + timedelta(days=1)).isoformat()

    client = monte_carlo_credentials.get_client()

    query = """
        mutation($destination_object_id: String!,
        $destination_object_type: String!,
        $destination_resource_name: String!,
        $source_object_id: String!, $source_object_type: String!,
            $source_resource_name: String!, $expire_at: DateTime) {
            createOrUpdateLineageEdge(
            destination: {
                objectId: $destination_object_id
                objectType: $destination_object_type
                resourceName: $destination_resource_name
            }
            source: {
                objectId: $source_object_id
                objectType: $source_object_type
                resourceName: $source_resource_name
            }
            expireAt: $expire_at
            ){
            edge{
                edgeId
            }
            }
        }
        """

    variables = dict(
        destination_object_id=destination["object_id"],
        destination_object_type=destination["object_type"],
        destination_resource_name=destination["resource_name"],
        source_object_id=source["object_id"],
        source_object_type=source["object_type"],
        source_resource_name=source["resource_name"],
        expire_at=expire_at,
    )

    return client(query=query, variables=variables)
