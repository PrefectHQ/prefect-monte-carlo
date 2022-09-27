"""
This is a module containing:
Montecarlo query_get_lineage_edge* tasks
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

from pathlib import Path
from typing import Any, Dict, Iterable

from prefect import task
from sgqlc.operation import Operation

from prefect_montecarlo import MontecarloCredentials
from prefect_montecarlo.graphql import _execute_graphql_op, _subset_return_fields
from prefect_montecarlo.schemas import graphql_schema
from prefect_montecarlo.utils import initialize_return_fields_defaults, strip_kwargs

config_path = (
    Path(__file__).parent.resolve() / "configs" / "query" / "get_lineage_edge.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_lineage_edge(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    source: graphql_schema.NodeInput = None,
    destination: graphql_schema.NodeInput = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        source: Source node.
        destination: Destination node.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_lineage_edge(
        **strip_kwargs(
            source=source,
            destination=destination,
        )
    )

    op_stack = ("getLineageEdge",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getLineageEdge"]


@task
async def query_get_lineage_edge_dest(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    source: graphql_schema.NodeInput = None,
    destination: graphql_schema.NodeInput = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Destination node MCON, downstream in the graph.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        source: Source node.
        destination: Destination node.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_lineage_edge(
        **strip_kwargs(
            source=source,
            destination=destination,
        )
    ).dest(**strip_kwargs())

    op_stack = (
        "getLineageEdge",
        "dest",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getLineageEdge"]["dest"]


@task
async def query_get_lineage_edge_source(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    source: graphql_schema.NodeInput = None,
    destination: graphql_schema.NodeInput = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Source node MCON, upstream in the graph.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        source: Source node.
        destination: Destination node.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_lineage_edge(
        **strip_kwargs(
            source=source,
            destination=destination,
        )
    ).source(**strip_kwargs())

    op_stack = (
        "getLineageEdge",
        "source",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getLineageEdge"]["source"]


@task
async def query_get_lineage_edge_last_update_user(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    source: graphql_schema.NodeInput = None,
    destination: graphql_schema.NodeInput = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Who last updated the edge.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        source: Source node.
        destination: Destination node.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_lineage_edge(
        **strip_kwargs(
            source=source,
            destination=destination,
        )
    ).last_update_user(**strip_kwargs())

    op_stack = (
        "getLineageEdge",
        "lastUpdateUser",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getLineageEdge"]["lastUpdateUser"]
