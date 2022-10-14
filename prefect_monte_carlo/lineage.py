""" Module to define tasks and flows for interacting with lineage resources. """

from datetime import datetime
from typing import Dict, List, Optional

from prefect import flow, get_run_logger, task
from pydantic import BaseModel, validator

from prefect_monte_carlo.credentials import MonteCarloCredentials
from prefect_monte_carlo.utilities import validate_tags


class MonteCarloLineageNode(BaseModel):
    """Pydantic Model of a Monte Carlo lineage lineage node."""

    node_name: str
    object_id: str
    resource_name: str
    object_type: Optional[str] = "table"
    tags: Optional[List[Dict[str, str]]] = None

    @validator("tags")
    def valid_tags(cls, tags):
        """Validate that tags are in the correct format."""
        validate_tags(tags)
        return tags


@flow(
    description="Create or update a `source` node, `destination` node, and the edge that connects them.",  # noqa: E501
)
async def create_or_update_lineage(
    monte_carlo_credentials: MonteCarloCredentials,
    source: MonteCarloLineageNode,
    destination: MonteCarloLineageNode,
    expire_at: Optional[datetime] = None,
    extra_tags: Optional[List] = None,
) -> str:
    """Task for creating or updating a lineage node for the given source
    and destination nodes, as well as for creating a lineage edge between those nodes.

    Args:
        monte_carlo_credentials: The Monte Carlo credentials block used to generate
            an authenticated GraphQL API client via pycarlo.
        source: A source node configuration - expected to include the following
            keys: `node_name`, `object_id`, `object_type`, `resource_name`, `tags`.
        destination: A destination node configuration - expected to include the
            following keys: `node_name`, `object_id`, `object_type`, `resource_name`,
            `tags`.
        expire_at: Date and time indicating when to expire
            a source-destination edge.
        extra_tags: Optional list of tags to attach to the source
            and destination node.

    Raises:
        ValueError: If the source or destination node configuration
            is missing `object_id` or `resource_name`.

    Returns:
        The ID of the lineage edge created or updated.

    Example:
        Create or update a lineage edge between a source and destination node.
        ```python
        from prefect import flow
        from prefect.context import get_run_context
        from prefect_monte_carlo.credentials import MonteCarloCredentials
        from prefect_monte_carlo.lineage import (
            create_or_update_lineage, MonteCarloLineageNode
        )

        @flow
        def monte_carlo_orchestrator():
            flow_run_name = get_run_context().flow_run.name

            source = MonteCarloLineageNode(
                node_name="source_dataset",
                object_id="source_dataset",
                object_type="table",
                resource_name="some_resource_name",
                tags=[{"propertyName": "dataset_owner", "propertyValue": "owner_name"}],
            )

            destination = MonteCarloLineageNode(
                node_name="destination_dataset",
                object_id="destination_dataset",
                object_type="table",
                resource_name="some_resource_name",
                tags=[{"propertyName": "dataset_owner", "propertyValue": "owner_name"}],
            )

            # `create_or_update_lineage` is a flow, so this will be a subflow run
            # `extra_tags` are added to both the `source` and `destination` nodes
            create_or_update_lineage(
                monte_carlo_credentials=MonteCarloCredentials.load("my-mc-creds)
                source=source,
                destination=destination,
                expire_at=datetime.now() + timedelta(days=10),
                extra_tags=[
                    {"propertyName": "flow_run_name", "propertyValue": flow_run_name}
                ]
            )

        ```
    """
    logger = get_run_logger()

    if extra_tags:
        validate_tags(extra_tags)
        source.tags = source.tags + extra_tags if source.tags else extra_tags
        destination.tags = (
            destination.tags + extra_tags if destination.tags else extra_tags
        )

    source_node_mcon = await create_or_update_lineage_node(
        monte_carlo_credentials=monte_carlo_credentials,
        node_name=source.node_name,
        object_id=source.object_id,
        object_type=source.object_type,
        resource_name=source.resource_name,
        tags=source.tags,
    )

    source_node_url = f"{monte_carlo_credentials.catalog_url}/{source_node_mcon}/table"
    logger.info("Created or updated a source lineage node %s", source_node_url)

    destination_node_mcon = await create_or_update_lineage_node(
        monte_carlo_credentials=monte_carlo_credentials,
        node_name=destination.node_name,
        object_id=destination.object_id,
        object_type=destination.object_type,
        resource_name=destination.resource_name,
        tags=destination.tags,
    )

    destination_node_url = (
        f"{monte_carlo_credentials.catalog_url}/{destination_node_mcon}/table"
    )
    logger.info(
        "Created or updated a destination lineage node %s", destination_node_url
    )

    # edge between source and destination nodes
    edge_id = await create_or_update_lineage_edge(
        monte_carlo_credentials=monte_carlo_credentials,
        source=source,
        destination=destination,
        expire_at=expire_at,
    )

    logger.info(f"Created or updated a destination lineage edge: {edge_id}")

    return edge_id


@task(
    retries=2,
    retry_delay_seconds=3,
    description="Create or update a Monte Carlo lineage node via the GraphQL API.",
)
async def create_or_update_lineage_node(
    monte_carlo_credentials: MonteCarloCredentials,
    node_name: str,
    object_id: str,
    object_type: str,
    resource_name: str,
    tags: Optional[List[Dict[str, str]]] = None,
) -> str:
    """Task for creating or updating a lineage node via the Monte Carlo GraphQL API.


    Args:
        monte_carlo_credentials: The Monte Carlo credentials block used to generate.
        node_name: The name of the lineage node.
        object_id: The object ID of the lineage node.
        object_type: The object type of the lineage node.
        resource_name: The resource name of the lineage node.
        tags: A list of tags to apply to the lineage node.

    Returns:
        The MCON identifying the lineage node.

    Example:
        Create or update a lineage node from a `MonteCarloLineageNode` object:
        ```python
        from prefect import flow
        from prefect_monte_carlo.credentials import MonteCarloCredentials
        from prefect_monte_carlo.lineage import (
            create_or_update_lineage_node, MonteCarloLineageNode
        )

        mc_node = MonteCarloLineageNode(
            node_name="source_node",
            object_id="my_source_object_id",
            object_type="table",
            resource_name="my_source_resource_name",
            tags=[{"propertyName": "tag_key", "propertyValue": "tag_value"}],
        )

        @flow
        def monte_carlo_lineage_flow():
            node_mcon = create_or_update_lineage_node(
                monte_carlo_credentials=MonteCarloCredentials.load("my-mc-creds"),
                **mc_node.dict(),

        ```
    """
    mc_client = monte_carlo_credentials.get_client()

    response = mc_client(
        query="""
        mutation($node_name: String!, $object_id: String!, $object_type: String!,
        $resource_name: String!, $tags: [ObjectPropertyInput]
        ) {
            createOrUpdateLineageNode(
            name: $node_name,
            objectId: $object_id,
            objectType: $object_type,
            resourceName: $resource_name,
            properties: $tags
            ){
                node{
                    mcon
                }
            }
        }
        """,
        variables=dict(
            node_name=node_name,
            object_id=object_id,
            object_type=object_type,
            resource_name=resource_name,
            tags=tags,
        ),
    )
    mcon_string = response["create_or_update_lineage_node"]["node"]["mcon"]
    return mcon_string


@task(
    retries=2,
    retry_delay_seconds=3,
    description="Create or update a Monte Carlo lineage edge via the GraphQL API.",
)
async def create_or_update_lineage_edge(
    monte_carlo_credentials: MonteCarloCredentials,
    source: MonteCarloLineageNode,
    destination: MonteCarloLineageNode,
    expire_at: Optional[datetime] = None,
) -> str:
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
        from prefect_monte_carlo.lineage import (
            create_or_update_lineage_edge, MonteCarloLineageNode
        )

        source = MonteCarloLineageNode(
            node_name="example_table_name",
            object_id="example_table_name",
            # "table" is recommended, but you can use any string, e.g. "csv_file"
            object_type="table",
            resource_name="name_your_source_system",
            tags=[{"propertyName": "key", "propertyValue": "value"}]
        )

        destination = MonteCarloLineageNode(
            node_name="db_name:schema_name.table_name",
            object_id="db_name:schema_name.table_name",
            object_type="table",
            resource_name="your_dwh_resource_name",
            tags=[{"propertyName": "key", "propertyValue": "value"}]
        )

        @flow
        def my_monte_carlo_flow():
            create_or_update_lineage_edge(
                source=source,
                destination=destination,
                monte_carlo_credentials=MonteCarloCredentials.load("my-mc-creds"),
                expire_at=datetime.now() + timedelta(days=10),
            )
        ```

    """
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
        destination_object_id=destination.object_id,
        destination_object_type=destination.object_type,
        destination_resource_name=destination.resource_name,
        source_object_id=source.object_id,
        source_object_type=source.object_type,
        source_resource_name=source.resource_name,
        expire_at=expire_at.isoformat() if expire_at else None,
    )

    response = client(query=query, variables=variables)

    edge_id = response["create_or_update_lineage_edge"]["edge"]["edge_id"]

    return edge_id
