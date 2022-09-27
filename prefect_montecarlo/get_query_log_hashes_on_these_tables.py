"""
This is a module containing:
Montecarlo query_get_query_log_hashes_on_these_tables* tasks
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
    Path(__file__).parent.resolve()
    / "configs"
    / "query"
    / "get_query_log_hashes_on_these_tables.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_query_log_hashes_on_these_tables(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_ids: Iterable[str] = None,
    mcons: Iterable[str] = None,
    limit: int = None,
    offset: int = None,
    start_time: datetime = None,
    end_time: datetime = None,
    users: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the tables are contained in. Required when using
            fullTableIds.
        full_table_ids: Deprecated - use mcons. Ignored if mcons are present.
        mcons: List of mcons to get details for.
        limit: Limit results returned.
        offset: Offset when paging.
        start_time: Filter for queries newer than this.
        end_time: Filter for queries older than this.
        users: List of users to get details for.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_query_log_hashes_on_these_tables(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_ids=full_table_ids,
            mcons=mcons,
            limit=limit,
            offset=offset,
            start_time=start_time,
            end_time=end_time,
            users=users,
        )
    )

    op_stack = ("getQueryLogHashesOnTheseTables",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getQueryLogHashesOnTheseTables"]


@task
async def query_get_query_log_hashes_on_these_tables_query_hashes(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_ids: Iterable[str] = None,
    mcons: Iterable[str] = None,
    limit: int = None,
    offset: int = None,
    start_time: datetime = None,
    end_time: datetime = None,
    users: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the tables are
            contained in. Required when using fullTableIds.
        full_table_ids: Deprecated - use
            mcons. Ignored if mcons are present.
        mcons: List of mcons to get details
            for.
        limit: Limit results returned.
        offset: Offset when paging.
        start_time: Filter for queries
            newer than this.
        end_time: Filter for queries older
            than this.
        users: List of users to get details
            for.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_query_log_hashes_on_these_tables(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_ids=full_table_ids,
            mcons=mcons,
            limit=limit,
            offset=offset,
            start_time=start_time,
            end_time=end_time,
            users=users,
        )
    ).query_hashes(**strip_kwargs())

    op_stack = (
        "getQueryLogHashesOnTheseTables",
        "queryHashes",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getQueryLogHashesOnTheseTables"]["queryHashes"]
