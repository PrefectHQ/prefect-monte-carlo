"""
This is a module containing:
Montecarlo query_get_query_list* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_query_list.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_query_list(  # noqa
    query_type: str,
    mcon: str,
    start_time: datetime,
    end_time: datetime,
    montecarlo_credentials: MontecarloCredentials,
    user_name: str = None,
    limit: int = None,
    offset: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        query_type: source (reads on the table) or destination (writes on this
            table).
        mcon: Monte Carlo object name.
        start_time: Filter for queries newer than this.
        end_time: Filter for queries older than this.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        user_name: Filter by user name.
        limit: Limit results returned.
        offset: Offset when paging.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_query_list(
        **strip_kwargs(
            query_type=query_type,
            mcon=mcon,
            start_time=start_time,
            end_time=end_time,
            user_name=user_name,
            limit=limit,
            offset=offset,
        )
    )

    op_stack = ("getQueryList",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getQueryList"]


@task
async def query_get_query_list_queries(  # noqa
    query_type: str,
    mcon: str,
    start_time: datetime,
    end_time: datetime,
    montecarlo_credentials: MontecarloCredentials,
    user_name: str = None,
    limit: int = None,
    offset: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        query_type: source (reads on the table) or destination
            (writes on this table).
        mcon: Monte Carlo object name.
        start_time: Filter for queries newer than this.
        end_time: Filter for queries older than this.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        user_name: Filter by user name.
        limit: Limit results returned.
        offset: Offset when paging.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_query_list(
        **strip_kwargs(
            query_type=query_type,
            mcon=mcon,
            start_time=start_time,
            end_time=end_time,
            user_name=user_name,
            limit=limit,
            offset=offset,
        )
    ).queries(**strip_kwargs())

    op_stack = (
        "getQueryList",
        "queries",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getQueryList"]["queries"]


@task
async def query_get_query_list_queries_by_type(  # noqa
    query_type: str,
    mcon: str,
    start_time: datetime,
    end_time: datetime,
    montecarlo_credentials: MontecarloCredentials,
    user_name: str = None,
    limit: int = None,
    offset: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        query_type: source (reads on the table) or destination
            (writes on this table).
        mcon: Monte Carlo object name.
        start_time: Filter for queries newer than this.
        end_time: Filter for queries older than this.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        user_name: Filter by user name.
        limit: Limit results returned.
        offset: Offset when paging.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_query_list(
        **strip_kwargs(
            query_type=query_type,
            mcon=mcon,
            start_time=start_time,
            end_time=end_time,
            user_name=user_name,
            limit=limit,
            offset=offset,
        )
    ).queries_by_type(**strip_kwargs())

    op_stack = (
        "getQueryList",
        "queriesByType",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getQueryList"]["queriesByType"]
