"""
This is a module containing:
Montecarlo query_get_monitors* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_monitors.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_monitors(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    monitor_types: Iterable[graphql_schema.UserDefinedMonitors] = None,
    status_types: Iterable[graphql_schema.MonitorStatusType] = None,
    description_field_or_table: Iterable[str] = None,
    domain_id: datetime = None,
    uuids: Iterable[str] = None,
    created_by_filters: graphql_schema.CreatedByFilters = None,
    labels: Iterable[str] = None,
    search: Iterable[str] = None,
    order_by: str = None,
    limit: int = None,
    offset: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        monitor_types: Type of monitors to filter by, default all.
        status_types: Type of monitor status to filter by, default all.
        description_field_or_table: DEPRECATED.
        domain_id: Domain uuid to filter by.
        uuids: list of uuids of the monitors to filter by.
        created_by_filters: Deprecated.
        labels: List of labels to filter by.
        search: search criteria for filtering the monitors list.
        order_by: Field and direction to order monitors by.
        limit: Number of monitors to return.
        offset: From which monitor to return the next results.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_monitors(
        **strip_kwargs(
            monitor_types=monitor_types,
            status_types=status_types,
            description_field_or_table=description_field_or_table,
            domain_id=domain_id,
            uuids=uuids,
            created_by_filters=created_by_filters,
            labels=labels,
            search=search,
            order_by=order_by,
            limit=limit,
            offset=offset,
        )
    )

    op_stack = ("getMonitors",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMonitors"]


@task
async def query_get_monitors_schedule_config(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    monitor_types: Iterable[graphql_schema.UserDefinedMonitors] = None,
    status_types: Iterable[graphql_schema.MonitorStatusType] = None,
    description_field_or_table: Iterable[str] = None,
    domain_id: datetime = None,
    uuids: Iterable[str] = None,
    created_by_filters: graphql_schema.CreatedByFilters = None,
    labels: Iterable[str] = None,
    search: Iterable[str] = None,
    order_by: str = None,
    limit: int = None,
    offset: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        monitor_types: Type of monitors to filter by, default all.
        status_types: Type of monitor status to filter by, default
            all.
        description_field_or_table: DEPRECATED.
        domain_id: Domain uuid to filter by.
        uuids: list of uuids of the monitors to filter by.
        created_by_filters: Deprecated.
        labels: List of labels to filter by.
        search: search criteria for filtering the monitors list.
        order_by: Field and direction to order monitors by.
        limit: Number of monitors to return.
        offset: From which monitor to return the next results.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_monitors(
        **strip_kwargs(
            monitor_types=monitor_types,
            status_types=status_types,
            description_field_or_table=description_field_or_table,
            domain_id=domain_id,
            uuids=uuids,
            created_by_filters=created_by_filters,
            labels=labels,
            search=search,
            order_by=order_by,
            limit=limit,
            offset=offset,
        )
    ).schedule_config(**strip_kwargs())

    op_stack = (
        "getMonitors",
        "scheduleConfig",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMonitors"]["scheduleConfig"]


@task
async def query_get_monitors_rule_comparisons(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    monitor_types: Iterable[graphql_schema.UserDefinedMonitors] = None,
    status_types: Iterable[graphql_schema.MonitorStatusType] = None,
    description_field_or_table: Iterable[str] = None,
    domain_id: datetime = None,
    uuids: Iterable[str] = None,
    created_by_filters: graphql_schema.CreatedByFilters = None,
    labels: Iterable[str] = None,
    search: Iterable[str] = None,
    order_by: str = None,
    limit: int = None,
    offset: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        monitor_types: Type of monitors to filter by, default all.
        status_types: Type of monitor status to filter by, default
            all.
        description_field_or_table: DEPRECATED.
        domain_id: Domain uuid to filter by.
        uuids: list of uuids of the monitors to filter by.
        created_by_filters: Deprecated.
        labels: List of labels to filter by.
        search: search criteria for filtering the monitors list.
        order_by: Field and direction to order monitors by.
        limit: Number of monitors to return.
        offset: From which monitor to return the next results.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_monitors(
        **strip_kwargs(
            monitor_types=monitor_types,
            status_types=status_types,
            description_field_or_table=description_field_or_table,
            domain_id=domain_id,
            uuids=uuids,
            created_by_filters=created_by_filters,
            labels=labels,
            search=search,
            order_by=order_by,
            limit=limit,
            offset=offset,
        )
    ).rule_comparisons(**strip_kwargs())

    op_stack = (
        "getMonitors",
        "ruleComparisons",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMonitors"]["ruleComparisons"]


@task
async def query_get_monitors_select_expressions(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    monitor_types: Iterable[graphql_schema.UserDefinedMonitors] = None,
    status_types: Iterable[graphql_schema.MonitorStatusType] = None,
    description_field_or_table: Iterable[str] = None,
    domain_id: datetime = None,
    uuids: Iterable[str] = None,
    created_by_filters: graphql_schema.CreatedByFilters = None,
    labels: Iterable[str] = None,
    search: Iterable[str] = None,
    order_by: str = None,
    limit: int = None,
    offset: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Monitor select expression.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        monitor_types: Type of monitors to filter by, default all.
        status_types: Type of monitor status to filter by, default
            all.
        description_field_or_table: DEPRECATED.
        domain_id: Domain uuid to filter by.
        uuids: list of uuids of the monitors to filter by.
        created_by_filters: Deprecated.
        labels: List of labels to filter by.
        search: search criteria for filtering the monitors list.
        order_by: Field and direction to order monitors by.
        limit: Number of monitors to return.
        offset: From which monitor to return the next results.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_monitors(
        **strip_kwargs(
            monitor_types=monitor_types,
            status_types=status_types,
            description_field_or_table=description_field_or_table,
            domain_id=domain_id,
            uuids=uuids,
            created_by_filters=created_by_filters,
            labels=labels,
            search=search,
            order_by=order_by,
            limit=limit,
            offset=offset,
        )
    ).select_expressions(**strip_kwargs())

    op_stack = (
        "getMonitors",
        "selectExpressions",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMonitors"]["selectExpressions"]
