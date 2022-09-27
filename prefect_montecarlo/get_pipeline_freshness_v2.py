"""
This is a module containing:
Montecarlo query_get_pipeline_freshness_v2* tasks
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
    / "get_pipeline_freshness_v2.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_pipeline_freshness_v2(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_ids: Iterable[str] = None,
    mcons: Iterable[str] = None,
    start_time: datetime = None,
    end_time: datetime = None,
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
        start_time: Filter for data newer than this.
        end_time: Filter for data older than this.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_pipeline_freshness_v2(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_ids=full_table_ids,
            mcons=mcons,
            start_time=start_time,
            end_time=end_time,
        )
    )

    op_stack = ("getPipelineFreshnessV2",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getPipelineFreshnessV2"]


@task
async def query_get_pipeline_freshness_v2_metric_values_by_table(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_ids: Iterable[str] = None,
    mcons: Iterable[str] = None,
    start_time: datetime = None,
    end_time: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the tables are contained in.
            Required when using fullTableIds.
        full_table_ids: Deprecated - use mcons.
            Ignored if mcons are present.
        mcons: List of mcons to get details for.
        start_time: Filter for data newer than this.
        end_time: Filter for data older than this.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_pipeline_freshness_v2(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_ids=full_table_ids,
            mcons=mcons,
            start_time=start_time,
            end_time=end_time,
        )
    ).metric_values_by_table(**strip_kwargs())

    op_stack = (
        "getPipelineFreshnessV2",
        "metricValuesByTable",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getPipelineFreshnessV2"]["metricValuesByTable"]
