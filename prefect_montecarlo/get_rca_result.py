"""
This is a module containing:
Montecarlo query_get_rca_result* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_rca_result.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_rca_result(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    event_uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        event_uuid: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_rca_result(
        **strip_kwargs(
            event_uuid=event_uuid,
        )
    )

    op_stack = ("getRcaResult",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getRcaResult"]


@task
async def query_get_rca_result_rca_data(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    event_uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        event_uuid: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_rca_result(
        **strip_kwargs(
            event_uuid=event_uuid,
        )
    ).rca_data(**strip_kwargs())

    op_stack = (
        "getRcaResult",
        "rcaData",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getRcaResult"]["rcaData"]


@task
async def query_get_rca_result_rca_data_v2(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    event_uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        event_uuid: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_rca_result(
        **strip_kwargs(
            event_uuid=event_uuid,
        )
    ).rca_data_v2(**strip_kwargs())

    op_stack = (
        "getRcaResult",
        "rcaDataV2",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getRcaResult"]["rcaDataV2"]
