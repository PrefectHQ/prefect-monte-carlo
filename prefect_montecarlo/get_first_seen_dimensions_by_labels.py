"""
This is a module containing:
Montecarlo query_get_first_seen_dimensions_by_labels* tasks
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
    / "get_first_seen_dimensions_by_labels.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_first_seen_dimensions_by_labels(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    field: str = None,
    labels: Iterable[str] = None,
    start_time: datetime = None,
    end_time: datetime = None,
    dimensions_filter: Iterable[graphql_schema.MetricDimensionFilter] = None,
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
        field: Field (column) to get measurements for.
        labels: Labels to get measurements for. Can be retrieved using
            getFirstSeenDimensionsByLabels.
        start_time: Filter for data newer than this.
        end_time: Filter for data older than this.
        dimensions_filter: Filter by a list of key/value dimension pairs.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_first_seen_dimensions_by_labels(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
            field=field,
            labels=labels,
            start_time=start_time,
            end_time=end_time,
            dimensions_filter=dimensions_filter,
        )
    )

    op_stack = ("getFirstSeenDimensionsByLabels",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getFirstSeenDimensionsByLabels"]
