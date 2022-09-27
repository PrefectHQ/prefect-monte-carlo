"""
This is a module containing:
Montecarlo query_get_incident_data_weekly* tasks
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
    / "get_incident_data_weekly.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_incident_data_weekly(  # noqa
    group_by: graphql_schema.IncidentGroupBy,
    montecarlo_credentials: MontecarloCredentials,
    domain_uuid: datetime = None,
    lookback_weeks: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        group_by: The value to group the incidents by.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        domain_uuid: The domain id to filter by.
        lookback_weeks: The number of weeks to aggregate data over.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_data_weekly(
        **strip_kwargs(
            group_by=group_by,
            domain_uuid=domain_uuid,
            lookback_weeks=lookback_weeks,
        )
    )

    op_stack = ("getIncidentDataWeekly",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentDataWeekly"]


@task
async def query_get_incident_data_weekly_weekly_data(  # noqa
    group_by: graphql_schema.IncidentGroupBy,
    montecarlo_credentials: MontecarloCredentials,
    domain_uuid: datetime = None,
    lookback_weeks: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    The weekly incident data.

    Args:
        group_by: The value to group the incidents by.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        domain_uuid: The domain id to filter by.
        lookback_weeks: The number of weeks to
            aggregate data over.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_data_weekly(
        **strip_kwargs(
            group_by=group_by,
            domain_uuid=domain_uuid,
            lookback_weeks=lookback_weeks,
        )
    ).weekly_data(**strip_kwargs())

    op_stack = (
        "getIncidentDataWeekly",
        "weeklyData",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentDataWeekly"]["weeklyData"]
