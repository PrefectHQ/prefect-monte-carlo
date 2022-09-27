"""
This is a module containing:
Montecarlo query_get_generated_rules* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_generated_rules.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_generated_rules(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    generated_by_uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        generated_by_uuid: Parent CustomRule UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_generated_rules(
        **strip_kwargs(
            generated_by_uuid=generated_by_uuid,
        )
    )

    op_stack = ("getGeneratedRules",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getGeneratedRules"]


@task
async def query_get_generated_rules_comparisons(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    generated_by_uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        generated_by_uuid: Parent CustomRule UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_generated_rules(
        **strip_kwargs(
            generated_by_uuid=generated_by_uuid,
        )
    ).comparisons(**strip_kwargs())

    op_stack = (
        "getGeneratedRules",
        "comparisons",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getGeneratedRules"]["comparisons"]


@task
async def query_get_generated_rules_generated_by(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    generated_by_uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        generated_by_uuid: Parent CustomRule UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_generated_rules(
        **strip_kwargs(
            generated_by_uuid=generated_by_uuid,
        )
    ).generated_by(**strip_kwargs())

    op_stack = (
        "getGeneratedRules",
        "generatedBy",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getGeneratedRules"]["generatedBy"]


@task
async def query_get_generated_rules_schedule_config(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    generated_by_uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        generated_by_uuid: Parent CustomRule UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_generated_rules(
        **strip_kwargs(
            generated_by_uuid=generated_by_uuid,
        )
    ).schedule_config(**strip_kwargs())

    op_stack = (
        "getGeneratedRules",
        "scheduleConfig",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getGeneratedRules"]["scheduleConfig"]


@task
async def query_get_generated_rules_data_collection_schedule_config(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    generated_by_uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        generated_by_uuid: Parent CustomRule UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_generated_rules(
        **strip_kwargs(
            generated_by_uuid=generated_by_uuid,
        )
    ).data_collection_schedule_config(**strip_kwargs())

    op_stack = (
        "getGeneratedRules",
        "dataCollectionScheduleConfig",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getGeneratedRules"]["dataCollectionScheduleConfig"]
