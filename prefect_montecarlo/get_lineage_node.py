"""
This is a module containing:
Montecarlo query_get_lineage_node* tasks
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable

from prefect import task
from sgqlc.operation import Operation

from prefect_montecarlo import MontecarloCredentials
from prefect_montecarlo.graphql import _execute_graphql_op, _subset_return_fields
from prefect_montecarlo.schemas import graphql_schema
from prefect_montecarlo.utils import initialize_return_fields_defaults, strip_kwargs

config_path = (
    Path(__file__).parent.resolve() / "configs" / "query" / "get_lineage_node.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_lineage_node(  # noqa
    object_type: str,
    object_id: str,
    montecarlo_credentials: MontecarloCredentials,
    resource_id: datetime = None,
    resource_name: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        object_type: Object type.
        object_id: Object identifier.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        resource_id: The id of the resource containing the node.
        resource_name: The name of the resource containing the node.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_lineage_node(
        **strip_kwargs(
            object_type=object_type,
            object_id=object_id,
            resource_id=resource_id,
            resource_name=resource_name,
        )
    )

    op_stack = ("getLineageNode",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getLineageNode"]


@task
async def query_get_lineage_node_last_update_user(  # noqa
    object_type: str,
    object_id: str,
    montecarlo_credentials: MontecarloCredentials,
    resource_id: datetime = None,
    resource_name: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Who last updated the node.

    Args:
        object_type: Object type.
        object_id: Object identifier.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        resource_id: The id of the resource containing the node.
        resource_name: The name of the resource containing the
            node.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_lineage_node(
        **strip_kwargs(
            object_type=object_type,
            object_id=object_id,
            resource_id=resource_id,
            resource_name=resource_name,
        )
    ).last_update_user(**strip_kwargs())

    op_stack = (
        "getLineageNode",
        "lastUpdateUser",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getLineageNode"]["lastUpdateUser"]
