"""
This is a module containing:
Montecarlo query_get_blast_radius_direct_queries* tasks
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
    / "get_blast_radius_direct_queries.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_blast_radius_direct_queries(  # noqa
    incident_id: datetime,
    lookback: graphql_schema.LookbackRange,
    montecarlo_credentials: MontecarloCredentials,
    after_key: graphql_schema.QueryAfterKeyInput = None,
    size: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        incident_id: The incident UUID.
        lookback: The lookback period for the blast radius [ONE_HOUR,
            TWELVE_HOUR, ONE_DAY, SEVEN_DAY].
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        after_key: The key for pagination.
        size: The max number of results to fetch.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_blast_radius_direct_queries(
        **strip_kwargs(
            incident_id=incident_id,
            lookback=lookback,
            after_key=after_key,
            size=size,
        )
    )

    op_stack = ("getBlastRadiusDirectQueries",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getBlastRadiusDirectQueries"]


@task
async def query_get_blast_radius_direct_queries_data(  # noqa
    incident_id: datetime,
    lookback: graphql_schema.LookbackRange,
    montecarlo_credentials: MontecarloCredentials,
    after_key: graphql_schema.QueryAfterKeyInput = None,
    size: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    The user blast radius data.

    Args:
        incident_id: The incident UUID.
        lookback: The lookback period for the
            blast radius [ONE_HOUR, TWELVE_HOUR, ONE_DAY, SEVEN_DAY].
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        after_key: The key for pagination.
        size: The max number of results to fetch.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_blast_radius_direct_queries(
        **strip_kwargs(
            incident_id=incident_id,
            lookback=lookback,
            after_key=after_key,
            size=size,
        )
    ).data(**strip_kwargs())

    op_stack = (
        "getBlastRadiusDirectQueries",
        "data",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getBlastRadiusDirectQueries"]["data"]


@task
async def query_get_blast_radius_direct_queries_after_key(  # noqa
    incident_id: datetime,
    lookback: graphql_schema.LookbackRange,
    montecarlo_credentials: MontecarloCredentials,
    after_key: graphql_schema.QueryAfterKeyInput = None,
    size: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    The after key to use for pagination.

    Args:
        incident_id: The incident UUID.
        lookback: The lookback period for the
            blast radius [ONE_HOUR, TWELVE_HOUR, ONE_DAY, SEVEN_DAY].
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        after_key: The key for pagination.
        size: The max number of results to fetch.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_blast_radius_direct_queries(
        **strip_kwargs(
            incident_id=incident_id,
            lookback=lookback,
            after_key=after_key,
            size=size,
        )
    ).after_key(**strip_kwargs())

    op_stack = (
        "getBlastRadiusDirectQueries",
        "afterKey",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getBlastRadiusDirectQueries"]["afterKey"]
