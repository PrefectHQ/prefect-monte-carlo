"""
This is a module containing:
Montecarlo query_get_dt_sampling* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_dt_sampling.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_dt_sampling(  # noqa
    monitor_uuid: datetime,
    montecarlo_credentials: MontecarloCredentials,
    start_time: datetime = None,
    dry_run: bool = False,
    limit: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        monitor_uuid: Monitor uuid is used for creating the sampling query.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        start_time: Event start time.
        dry_run: Generate sample query without running.
        limit: Limit results.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_dt_sampling(
        **strip_kwargs(
            monitor_uuid=monitor_uuid,
            start_time=start_time,
            dry_run=dry_run,
            limit=limit,
        )
    )

    op_stack = ("getDtSampling",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDtSampling"]
