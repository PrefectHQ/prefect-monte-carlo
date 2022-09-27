"""
This is a module containing:
Montecarlo query_get_incident_type_summary* tasks
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
    / "get_incident_type_summary.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_incident_type_summary(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    start_time: datetime = None,
    end_time: datetime = None,
    domain_id: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Filter by a specific warehouse.
        start_time: Filter for incidents newer than this.
        end_time: Filter for incidents older than this.
        domain_id: Filter by domain UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_type_summary(
        **strip_kwargs(
            dw_id=dw_id,
            start_time=start_time,
            end_time=end_time,
            domain_id=domain_id,
        )
    )

    op_stack = ("getIncidentTypeSummary",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentTypeSummary"]
