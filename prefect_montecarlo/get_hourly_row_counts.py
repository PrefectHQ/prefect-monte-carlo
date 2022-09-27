"""
This is a module containing:
Montecarlo query_get_hourly_row_counts* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_hourly_row_counts.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_hourly_row_counts(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    interval_days: int = 2,
    field_name: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in. Required when using a
            fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is present.
        mcon: Mcon for table to get details for.
        interval_days: Number of days to retrieve row counts for.
        field_name: Time axis to use - If not specified, first found is used.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_hourly_row_counts(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
            interval_days=interval_days,
            field_name=field_name,
        )
    )

    op_stack = ("getHourlyRowCounts",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getHourlyRowCounts"]


@task
async def query_get_hourly_row_counts_time_axis(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    interval_days: int = 2,
    field_name: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in.
            Required when using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if
            mcon is present.
        mcon: Mcon for table to get details for.
        interval_days: Number of days to retrieve row
            counts for.
        field_name: Time axis to use - If not specified,
            first found is used.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_hourly_row_counts(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
            interval_days=interval_days,
            field_name=field_name,
        )
    ).time_axis(**strip_kwargs())

    op_stack = (
        "getHourlyRowCounts",
        "timeAxis",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getHourlyRowCounts"]["timeAxis"]


@task
async def query_get_hourly_row_counts_hourly_counts(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    interval_days: int = 2,
    field_name: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in.
            Required when using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if
            mcon is present.
        mcon: Mcon for table to get details for.
        interval_days: Number of days to retrieve row
            counts for.
        field_name: Time axis to use - If not specified,
            first found is used.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_hourly_row_counts(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
            interval_days=interval_days,
            field_name=field_name,
        )
    ).hourly_counts(**strip_kwargs())

    op_stack = (
        "getHourlyRowCounts",
        "hourlyCounts",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getHourlyRowCounts"]["hourlyCounts"]
