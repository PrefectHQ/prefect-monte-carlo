"""
This is a module containing:
Montecarlo query_get_dt_reproduction_query* tasks
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
    / "get_dt_reproduction_query.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_dt_reproduction_query(  # noqa
    monitor_uuid: datetime,
    event_created_time: datetime,
    field: str,
    field_val: str,
    montecarlo_credentials: MontecarloCredentials,
    dry_run: bool = True,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        monitor_uuid: UUID of the monitor on which the anomaly occurred.
        event_created_time: When the anomaly occurred.
        field: The field on which the anomaly was found.
        field_val: The value for which the anomaly was found.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dry_run: Generate sample query without running.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_dt_reproduction_query(
        **strip_kwargs(
            monitor_uuid=monitor_uuid,
            event_created_time=event_created_time,
            field=field,
            field_val=field_val,
            dry_run=dry_run,
        )
    )

    op_stack = ("getDtReproductionQuery",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDtReproductionQuery"]
