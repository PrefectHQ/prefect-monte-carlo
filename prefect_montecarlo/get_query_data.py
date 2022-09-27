"""
This is a module containing:
Montecarlo query_get_query_data* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_query_data.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_query_data(  # noqa
    day: datetime,
    montecarlo_credentials: MontecarloCredentials,
    query_id: str = None,
    query_hash: str = None,
    limit: int = None,
    offset: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        day: The day for which to fetch the query metadata.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        query_id: The query_id for which to fetch the queries.
        query_hash: The query_hash for which to fetch the queries.
        limit: Limit results returned.
        offset: Offset when paging.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_query_data(
        **strip_kwargs(
            day=day,
            query_id=query_id,
            query_hash=query_hash,
            limit=limit,
            offset=offset,
        )
    )

    op_stack = ("getQueryData",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getQueryData"]


@task
async def query_get_query_data_queries(  # noqa
    day: datetime,
    montecarlo_credentials: MontecarloCredentials,
    query_id: str = None,
    query_hash: str = None,
    limit: int = None,
    offset: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        day: The day for which to fetch the query metadata.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        query_id: The query_id for which to fetch the queries.
        query_hash: The query_hash for which to fetch the queries.
        limit: Limit results returned.
        offset: Offset when paging.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_query_data(
        **strip_kwargs(
            day=day,
            query_id=query_id,
            query_hash=query_hash,
            limit=limit,
            offset=offset,
        )
    ).queries(**strip_kwargs())

    op_stack = (
        "getQueryData",
        "queries",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getQueryData"]["queries"]


@task
async def query_get_query_data_query_data(  # noqa
    day: datetime,
    montecarlo_credentials: MontecarloCredentials,
    query_id: str = None,
    query_hash: str = None,
    limit: int = None,
    offset: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        day: The day for which to fetch the query metadata.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        query_id: The query_id for which to fetch the queries.
        query_hash: The query_hash for which to fetch the queries.
        limit: Limit results returned.
        offset: Offset when paging.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_query_data(
        **strip_kwargs(
            day=day,
            query_id=query_id,
            query_hash=query_hash,
            limit=limit,
            offset=offset,
        )
    ).query_data(**strip_kwargs())

    op_stack = (
        "getQueryData",
        "queryData",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getQueryData"]["queryData"]
