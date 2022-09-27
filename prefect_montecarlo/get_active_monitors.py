"""
This is a module containing:
Montecarlo query_get_active_monitors* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_active_monitors.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_active_monitors(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    entities: str = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        entities: Filter by full table id or mcon.
        before: None.
        after: None.
        first: None.
        last: None.
        type: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_active_monitors(
        **strip_kwargs(
            entities=entities,
            before=before,
            after=after,
            first=first,
            last=last,
            type=type,
        )
    )

    op_stack = ("getActiveMonitors",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getActiveMonitors"]


@task
async def query_get_active_monitors_edges(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    entities: str = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Contains the nodes in this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        entities: Filter by full table id or mcon.
        before: None.
        after: None.
        first: None.
        last: None.
        type: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_active_monitors(
        **strip_kwargs(
            entities=entities,
            before=before,
            after=after,
            first=first,
            last=last,
            type=type,
        )
    ).edges(**strip_kwargs())

    op_stack = (
        "getActiveMonitors",
        "edges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getActiveMonitors"]["edges"]


@task
async def query_get_active_monitors_page_info(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    entities: str = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Pagination data for this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        entities: Filter by full table id or mcon.
        before: None.
        after: None.
        first: None.
        last: None.
        type: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_active_monitors(
        **strip_kwargs(
            entities=entities,
            before=before,
            after=after,
            first=first,
            last=last,
            type=type,
        )
    ).page_info(**strip_kwargs())

    op_stack = (
        "getActiveMonitors",
        "pageInfo",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getActiveMonitors"]["pageInfo"]
