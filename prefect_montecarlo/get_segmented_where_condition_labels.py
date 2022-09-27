"""
This is a module containing:
Montecarlo query_get_segmented_where_condition_labels* tasks
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
    / "get_segmented_where_condition_labels.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_segmented_where_condition_labels(  # noqa
    monitor_uuid: datetime,
    warehouse_uuid: datetime,
    full_table_id: str,
    start_time: datetime,
    montecarlo_credentials: MontecarloCredentials,
    end_time: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        monitor_uuid: The monitor for which to locate labels.
        warehouse_uuid: The warehouse uuid the monitor is being run on.
        full_table_id: The table being monitored.
        start_time: Filter for labels from this date.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        end_time: Filter for labels until and including this date.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_segmented_where_condition_labels(
        **strip_kwargs(
            monitor_uuid=monitor_uuid,
            warehouse_uuid=warehouse_uuid,
            full_table_id=full_table_id,
            start_time=start_time,
            end_time=end_time,
        )
    )

    op_stack = ("getSegmentedWhereConditionLabels",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getSegmentedWhereConditionLabels"]
