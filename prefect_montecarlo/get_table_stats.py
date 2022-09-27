"""
This is a module containing:
Montecarlo query_get_table_stats* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_table_stats.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_table_stats(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_ids: Iterable[str] = None,
    mcons: Iterable[str] = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Filter by warehouse. Required when using a fullTableId.
        full_table_ids: Deprecated - use mcon. Ignored if mcon is present.
        mcons: Get stats for specific tables by mcon.
        before: None.
        after: None.
        first: None.
        last: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table_stats(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_ids=full_table_ids,
            mcons=mcons,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    )

    op_stack = ("getTableStats",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTableStats"]


@task
async def query_get_table_stats_edges(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_ids: Iterable[str] = None,
    mcons: Iterable[str] = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Contains the nodes in this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Filter by warehouse. Required when using a
            fullTableId.
        full_table_ids: Deprecated - use mcon. Ignored if mcon
            is present.
        mcons: Get stats for specific tables by mcon.
        before: None.
        after: None.
        first: None.
        last: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table_stats(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_ids=full_table_ids,
            mcons=mcons,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).edges(**strip_kwargs())

    op_stack = (
        "getTableStats",
        "edges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTableStats"]["edges"]


@task
async def query_get_table_stats_page_info(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_ids: Iterable[str] = None,
    mcons: Iterable[str] = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Pagination data for this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Filter by warehouse. Required when using a
            fullTableId.
        full_table_ids: Deprecated - use mcon. Ignored if mcon
            is present.
        mcons: Get stats for specific tables by mcon.
        before: None.
        after: None.
        first: None.
        last: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table_stats(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_ids=full_table_ids,
            mcons=mcons,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).page_info(**strip_kwargs())

    op_stack = (
        "getTableStats",
        "pageInfo",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTableStats"]["pageInfo"]
