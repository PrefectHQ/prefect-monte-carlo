""" Module to defines tasks interacting with Monte Carlo lineage resources. """

from datetime import datetime
from typing import Any, Dict, List, Optional

import box
from prefect import get_run_logger, task
from prefect.context import get_run_context
from prefect.exceptions import MissingContextError

from prefect_monte_carlo.credentials import MonteCarloCredentials


class MonteCarloIncorrectTagsFormat(Exception):
    """Exception for incorrect tags format"""

    pass


def validate_tags(tags: List[Dict[str, str]]):
    for tag in tags:
        if sorted(tag.keys()) != ["propertyName", "propertyValue"]:
            raise MonteCarloIncorrectTagsFormat(
                "Must provide tags in the format "
                '[{"propertyName": "tag_name", "propertyValue": "tag_value"}].',
                "You provided: ",
                tag,
            )


@task
def create_or_update_lineage(
    monte_carlo_credentials: MonteCarloCredentials,
    source: Dict[str, Any],
    destination: Dict[str, Any],
    expire_at: Optional[datetime] = None,
    include_prefect_context_tags: Optional[bool] = False,
) -> box.BoxList:
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
        include_prefect_context_tags: Whether to include the Prefect context tags.

    Raises:
        ValueError: If the source or destination node configuration
            is missing `object_id` or `resource_name`.

    Returns:
        box.BoxList: Metadata for edge created between `source` and `destination` nodes.
    """
    logger = get_run_logger()

    if not ("node_name" in source and "node_name" in destination):
        raise ValueError("Must provide a `node_name` in both source and destination.")

    if not ("object_id" in source and "object_id" in destination):
        raise ValueError("Must provide an `object_id` in both source and destination.")

    if not ("resource_name" in source and "resource_name" in destination):
        raise ValueError(
            "Must provide a `resource_name` in both source and destination."
        )

    if "object_type" not in source:
        source["object_type"] = "table"

    if "object_type" not in destination:
        destination["object_type"] = "table"

    if "tags" in source:
        validate_tags(source["tags"])
        if include_prefect_context_tags:
            source["tags"] += get_prefect_context_tags()
    if "tags" in destination:
        validate_tags(destination["tags"])
        if include_prefect_context_tags:
            destination["tags"] += get_prefect_context_tags()

    source_node_mcon = create_or_update_lineage_node.fn(
        monte_carlo_credentials=monte_carlo_credentials,
        node_name=source["node_name"],
        object_id=source["object_id"],
        object_type=source["object_type"],
        resource_name=source["resource_name"],
        tags=source["tags"],
    )

    source_node_url = f"{monte_carlo_credentials.catalog_url}/{source_node_mcon}/table"
    logger.info("Created or updated a source lineage node %s", source_node_url)

    destination_node_mcon = create_or_update_lineage_node.fn(
        monte_carlo_credentials=monte_carlo_credentials,
        node_name=destination["node_name"],
        object_id=destination["object_id"],
        object_type=destination["object_type"],
        resource_name=destination["resource_name"],
        tags=destination["tags"],
    )

    destination_node_url = (
        f"{monte_carlo_credentials.catalog_url}/{destination_node_mcon}/table"
    )
    logger.info(
        "Created or updated a destination lineage node %s", destination_node_url
    )

    # edge between source and destination nodes
    edge_id = create_or_update_lineage_edge.fn(
        monte_carlo_credentials=monte_carlo_credentials,
        source=source,
        destination=destination,
        expire_at=expire_at.isoformat(),
    )

    logger.info("Created or updated a destination lineage edge %s", edge_id)

    return edge_id


@task
def create_or_update_lineage_node(
    monte_carlo_credentials: MonteCarloCredentials,
    node_name: str,
    object_id: str,
    object_type: str,
    resource_name: str,
    tags: Optional[List[Dict[str, str]]] = None,
) -> box.Box:
    """Task for creating or updating a lineage node via the Monte Carlo GraphQL API.

    Args:
        monte_carlo_credentials: The Monte Carlo credentials block used to generate.
        node_name: The name of the lineage node.
        object_id: The object ID of the lineage node.
        object_type: The object type of the lineage node.
        resource_name: The resource name of the lineage node.
        tags: A list of tags to apply to the lineage node.

    Returns:
        box.Box: The response from the GraphQL API.
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
    return response


@task
def create_or_update_lineage_edge(
    source: Dict[str, Any],
    destination: Dict[str, Any],
    monte_carlo_credentials: MonteCarloCredentials,
    expire_at: Optional[datetime] = None,
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


def get_prefect_context_tags() -> List[Dict[str, str]]:
    """Get the Prefect context tags from the current Prefect context.

    Returns:
        A list of tags in the format expected by the Monte Carlo GraphQL API.
    """
    try:
        return [  # rudimentary set of tags
            dict(propertyName=key, propertyValue=str(value))
            for key, value in get_run_context().task_run.dict().items()
        ]
    except MissingContextError:
        # TODO: Log a warning here?
        raise
