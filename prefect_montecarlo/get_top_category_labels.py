"""
This is a module containing:
Montecarlo query_get_top_category_labels* tasks
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
    / "get_top_category_labels.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_top_category_labels(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    monitor_ids: Iterable[str] = None,
    field: str = None,
    start_time: datetime = None,
    limit: int = None,
    end_time: datetime = None,
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
        monitor_ids: Filter results by monitor ID.
        field: Field (column) to get labels for.
        start_time: Filter for data newer than this.
        limit: Limit results retrieved.
        end_time: Filter for data older than this.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_top_category_labels(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
            monitor_ids=monitor_ids,
            field=field,
            start_time=start_time,
            limit=limit,
            end_time=end_time,
        )
    )

    op_stack = ("getTopCategoryLabels",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTopCategoryLabels"]
