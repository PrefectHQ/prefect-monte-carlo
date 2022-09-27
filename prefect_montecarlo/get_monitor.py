"""
This is a module containing:
Montecarlo query_get_monitor* tasks
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

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "get_monitor.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_monitor(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    resource_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    monitor_type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: Get monitor by UUID.
        resource_id: Specify the resource uuid (e.g. warehouse the table is
            contained in) when using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is present.
        mcon: Get monitor by mcon.
        monitor_type: Specify the monitor type. Required when using an mcon or
            full table id.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_monitor(
        **strip_kwargs(
            uuid=uuid,
            resource_id=resource_id,
            full_table_id=full_table_id,
            mcon=mcon,
            monitor_type=monitor_type,
        )
    )

    op_stack = ("getMonitor",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMonitor"]


@task
async def query_get_monitor_table(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    resource_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    monitor_type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Table related to monitor.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: Get monitor by UUID.
        resource_id: Specify the resource uuid (e.g. warehouse the
            table is contained in) when using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Get monitor by mcon.
        monitor_type: Specify the monitor type. Required when using
            an mcon or full table id.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_monitor(
        **strip_kwargs(
            uuid=uuid,
            resource_id=resource_id,
            full_table_id=full_table_id,
            mcon=mcon,
            monitor_type=monitor_type,
        )
    ).table(**strip_kwargs())

    op_stack = (
        "getMonitor",
        "table",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMonitor"]["table"]


@task
async def query_get_monitor_labels(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    resource_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    monitor_type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: Get monitor by UUID.
        resource_id: Specify the resource uuid (e.g. warehouse the
            table is contained in) when using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Get monitor by mcon.
        monitor_type: Specify the monitor type. Required when using
            an mcon or full table id.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_monitor(
        **strip_kwargs(
            uuid=uuid,
            resource_id=resource_id,
            full_table_id=full_table_id,
            mcon=mcon,
            monitor_type=monitor_type,
        )
    ).labels(**strip_kwargs())

    op_stack = (
        "getMonitor",
        "labels",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMonitor"]["labels"]


@task
async def query_get_monitor_schedule(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    resource_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    monitor_type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: Get monitor by UUID.
        resource_id: Specify the resource uuid (e.g. warehouse the
            table is contained in) when using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Get monitor by mcon.
        monitor_type: Specify the monitor type. Required when using
            an mcon or full table id.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_monitor(
        **strip_kwargs(
            uuid=uuid,
            resource_id=resource_id,
            full_table_id=full_table_id,
            mcon=mcon,
            monitor_type=monitor_type,
        )
    ).schedule(**strip_kwargs())

    op_stack = (
        "getMonitor",
        "schedule",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMonitor"]["schedule"]


@task
async def query_get_monitor_created_by(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    resource_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    monitor_type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Who added the monitor.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: Get monitor by UUID.
        resource_id: Specify the resource uuid (e.g. warehouse the
            table is contained in) when using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Get monitor by mcon.
        monitor_type: Specify the monitor type. Required when using
            an mcon or full table id.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_monitor(
        **strip_kwargs(
            uuid=uuid,
            resource_id=resource_id,
            full_table_id=full_table_id,
            mcon=mcon,
            monitor_type=monitor_type,
        )
    ).created_by(**strip_kwargs())

    op_stack = (
        "getMonitor",
        "createdBy",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMonitor"]["createdBy"]


@task
async def query_get_monitor_schedule_config(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    resource_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    monitor_type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: Get monitor by UUID.
        resource_id: Specify the resource uuid (e.g. warehouse the
            table is contained in) when using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Get monitor by mcon.
        monitor_type: Specify the monitor type. Required when using
            an mcon or full table id.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_monitor(
        **strip_kwargs(
            uuid=uuid,
            resource_id=resource_id,
            full_table_id=full_table_id,
            mcon=mcon,
            monitor_type=monitor_type,
        )
    ).schedule_config(**strip_kwargs())

    op_stack = (
        "getMonitor",
        "scheduleConfig",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMonitor"]["scheduleConfig"]


@task
async def query_get_monitor_select_expressions(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    resource_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    monitor_type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: Get monitor by UUID.
        resource_id: Specify the resource uuid (e.g. warehouse the
            table is contained in) when using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Get monitor by mcon.
        monitor_type: Specify the monitor type. Required when using
            an mcon or full table id.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_monitor(
        **strip_kwargs(
            uuid=uuid,
            resource_id=resource_id,
            full_table_id=full_table_id,
            mcon=mcon,
            monitor_type=monitor_type,
        )
    ).select_expressions(**strip_kwargs())

    op_stack = (
        "getMonitor",
        "selectExpressions",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMonitor"]["selectExpressions"]
