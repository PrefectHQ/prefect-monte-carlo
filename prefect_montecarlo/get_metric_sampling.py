"""
This is a module containing:
Montecarlo query_get_metric_sampling* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_metric_sampling.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_metric_sampling(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    time_axis: str = None,
    field: str = None,
    metric: str = None,
    start_time: datetime = None,
    end_time: datetime = None,
    limit: int = None,
    dry_run: bool = False,
    monitor_uuid: datetime = None,
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
        time_axis: Time field (column) to use when for date range.
        field: Field to sample for.
        metric: Type of metric to sample for.
        start_time: Filter for data newer than this.
        end_time: Filter for data older than this.
        limit: Limit results.
        dry_run: Generate sample query without running.
        monitor_uuid: Monitor uuid is used for extracting an accurate time axis.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_metric_sampling(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
            time_axis=time_axis,
            field=field,
            metric=metric,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            dry_run=dry_run,
            monitor_uuid=monitor_uuid,
        )
    )

    op_stack = ("getMetricSampling",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMetricSampling"]
