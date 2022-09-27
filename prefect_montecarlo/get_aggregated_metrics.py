"""
This is a module containing:
Montecarlo query_get_aggregated_metrics* tasks
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
    / "get_aggregated_metrics.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_aggregated_metrics(  # noqa
    dw_id: datetime,
    full_table_id_list: Iterable[str],
    metric: str,
    montecarlo_credentials: MontecarloCredentials,
    start_time: datetime = None,
    end_time: datetime = None,
    date_aggregation_bucket_size: str = "day",
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        dw_id: Warehouse the table is contained in. Required when using a
            fullTableId.
        full_table_id_list: Full table ID.
        metric: Type of metric.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        start_time: Filter for data newer than this.
        end_time: Filter for data older than this.
        date_aggregation_bucket_size: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_aggregated_metrics(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id_list=full_table_id_list,
            metric=metric,
            start_time=start_time,
            end_time=end_time,
            date_aggregation_bucket_size=date_aggregation_bucket_size,
        )
    )

    op_stack = ("getAggregatedMetrics",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getAggregatedMetrics"]


@task
async def query_get_aggregated_metrics_metrics(  # noqa
    dw_id: datetime,
    full_table_id_list: Iterable[str],
    metric: str,
    montecarlo_credentials: MontecarloCredentials,
    start_time: datetime = None,
    end_time: datetime = None,
    date_aggregation_bucket_size: str = "day",
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        dw_id: Warehouse the table is contained in.
            Required when using a fullTableId.
        full_table_id_list: Full table ID.
        metric: Type of metric.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        start_time: Filter for data newer than this.
        end_time: Filter for data older than this.
        date_aggregation_bucket_size: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_aggregated_metrics(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id_list=full_table_id_list,
            metric=metric,
            start_time=start_time,
            end_time=end_time,
            date_aggregation_bucket_size=date_aggregation_bucket_size,
        )
    ).metrics(**strip_kwargs())

    op_stack = (
        "getAggregatedMetrics",
        "metrics",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getAggregatedMetrics"]["metrics"]
