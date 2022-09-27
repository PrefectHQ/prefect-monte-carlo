"""
This is a module containing:
Montecarlo query_get_incident_summaries* tasks
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
    / "get_incident_summaries.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_incident_summaries(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    incident_ids: Iterable[datetime] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        incident_ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_summaries(
        **strip_kwargs(
            incident_ids=incident_ids,
        )
    )

    op_stack = ("getIncidentSummaries",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentSummaries"]


@task
async def query_get_incident_summaries_types(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    incident_ids: Iterable[datetime] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        incident_ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_summaries(
        **strip_kwargs(
            incident_ids=incident_ids,
        )
    ).types(**strip_kwargs())

    op_stack = (
        "getIncidentSummaries",
        "types",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentSummaries"]["types"]


@task
async def query_get_incident_summaries_states(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    incident_ids: Iterable[datetime] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        incident_ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_summaries(
        **strip_kwargs(
            incident_ids=incident_ids,
        )
    ).states(**strip_kwargs())

    op_stack = (
        "getIncidentSummaries",
        "states",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentSummaries"]["states"]
