"""
This is a module containing:
Montecarlo query_get_custom_rule* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_custom_rule.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_custom_rule(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    rule_id: datetime = None,
    description_contains: str = None,
    custom_sql_contains: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        rule_id: Rule id.
        description_contains: String to completely or partially match the rule
            description, case-insensitive.
        custom_sql_contains: String to completely or partially match the rule
            SQL, case-insensitive.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_custom_rule(
        **strip_kwargs(
            rule_id=rule_id,
            description_contains=description_contains,
            custom_sql_contains=custom_sql_contains,
        )
    )

    op_stack = ("getCustomRule",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getCustomRule"]


@task
async def query_get_custom_rule_comparisons(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    rule_id: datetime = None,
    description_contains: str = None,
    custom_sql_contains: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        rule_id: Rule id.
        description_contains: String to completely or partially
            match the rule description, case-insensitive.
        custom_sql_contains: String to completely or partially
            match the rule SQL, case-insensitive.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_custom_rule(
        **strip_kwargs(
            rule_id=rule_id,
            description_contains=description_contains,
            custom_sql_contains=custom_sql_contains,
        )
    ).comparisons(**strip_kwargs())

    op_stack = (
        "getCustomRule",
        "comparisons",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getCustomRule"]["comparisons"]


@task
async def query_get_custom_rule_schedule_config(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    rule_id: datetime = None,
    description_contains: str = None,
    custom_sql_contains: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        rule_id: Rule id.
        description_contains: String to completely or partially
            match the rule description, case-insensitive.
        custom_sql_contains: String to completely or partially
            match the rule SQL, case-insensitive.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_custom_rule(
        **strip_kwargs(
            rule_id=rule_id,
            description_contains=description_contains,
            custom_sql_contains=custom_sql_contains,
        )
    ).schedule_config(**strip_kwargs())

    op_stack = (
        "getCustomRule",
        "scheduleConfig",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getCustomRule"]["scheduleConfig"]


@task
async def query_get_custom_rule_data_collection_schedule_config(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    rule_id: datetime = None,
    description_contains: str = None,
    custom_sql_contains: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        rule_id: Rule id.
        description_contains: String to completely or partially
            match the rule description, case-insensitive.
        custom_sql_contains: String to completely or partially
            match the rule SQL, case-insensitive.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_custom_rule(
        **strip_kwargs(
            rule_id=rule_id,
            description_contains=description_contains,
            custom_sql_contains=custom_sql_contains,
        )
    ).data_collection_schedule_config(**strip_kwargs())

    op_stack = (
        "getCustomRule",
        "dataCollectionScheduleConfig",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getCustomRule"]["dataCollectionScheduleConfig"]
