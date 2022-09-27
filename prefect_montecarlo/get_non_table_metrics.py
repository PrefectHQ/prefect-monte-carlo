"""
This is a module containing:
Montecarlo query_get_non_table_metrics* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_non_table_metrics.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_non_table_metrics(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    mcon: str = None,
    metric: str = None,
    start_time: datetime = None,
    end_time: datetime = None,
    first: int = None,
    dimension_filters: Iterable[graphql_schema.MetricDimensionFilter] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in.
        mcon: the mcon associated with the metric.
        metric: Type of metric (e.g. row_count).
        start_time: Filter for data newer than this.
        end_time: Filter for data older than this.
        first: Number of metrics to retrieve.
        dimension_filters: Filter by a list of key/value dimension pairs.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_non_table_metrics(
        **strip_kwargs(
            dw_id=dw_id,
            mcon=mcon,
            metric=metric,
            start_time=start_time,
            end_time=end_time,
            first=first,
            dimension_filters=dimension_filters,
        )
    )

    op_stack = ("getNonTableMetrics",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getNonTableMetrics"]


@task
async def query_get_non_table_metrics_metrics(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    mcon: str = None,
    metric: str = None,
    start_time: datetime = None,
    end_time: datetime = None,
    first: int = None,
    dimension_filters: Iterable[graphql_schema.MetricDimensionFilter] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in.
        mcon: the mcon associated with the metric.
        metric: Type of metric (e.g. row_count).
        start_time: Filter for data newer than this.
        end_time: Filter for data older than this.
        first: Number of metrics to retrieve.
        dimension_filters: Filter by a list of key/value
            dimension pairs.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_non_table_metrics(
        **strip_kwargs(
            dw_id=dw_id,
            mcon=mcon,
            metric=metric,
            start_time=start_time,
            end_time=end_time,
            first=first,
            dimension_filters=dimension_filters,
        )
    ).metrics(**strip_kwargs())

    op_stack = (
        "getNonTableMetrics",
        "metrics",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getNonTableMetrics"]["metrics"]
