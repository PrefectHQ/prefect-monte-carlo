"""
This is a module containing:
Montecarlo query_get_event* tasks
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

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "get_event.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_event(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_event(
        **strip_kwargs(
            uuid=uuid,
        )
    )

    op_stack = ("getEvent",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getEvent"]


@task
async def query_get_event_ack_by(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_event(
        **strip_kwargs(
            uuid=uuid,
        )
    ).ack_by(**strip_kwargs())

    op_stack = (
        "getEvent",
        "ackBy",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getEvent"]["ackBy"]


@task
async def query_get_event_table(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_event(
        **strip_kwargs(
            uuid=uuid,
        )
    ).table(**strip_kwargs())

    op_stack = (
        "getEvent",
        "table",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getEvent"]["table"]


@task
async def query_get_event_anomaly(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_event(
        **strip_kwargs(
            uuid=uuid,
        )
    ).anomaly(**strip_kwargs())

    op_stack = (
        "getEvent",
        "anomaly",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getEvent"]["anomaly"]


@task
async def query_get_event_rca_jobs(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_event(
        **strip_kwargs(
            uuid=uuid,
        )
    ).rca_jobs(**strip_kwargs())

    op_stack = (
        "getEvent",
        "rcaJobs",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getEvent"]["rcaJobs"]


@task
async def query_get_event_incident(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_event(
        **strip_kwargs(
            uuid=uuid,
        )
    ).incident(**strip_kwargs())

    op_stack = (
        "getEvent",
        "incident",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getEvent"]["incident"]


@task
async def query_get_event_warehouse(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_event(
        **strip_kwargs(
            uuid=uuid,
        )
    ).warehouse(**strip_kwargs())

    op_stack = (
        "getEvent",
        "warehouse",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getEvent"]["warehouse"]


@task
async def query_get_event_table_stats(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Stats for the table connected to the event.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_event(
        **strip_kwargs(
            uuid=uuid,
        )
    ).table_stats(**strip_kwargs())

    op_stack = (
        "getEvent",
        "tableStats",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getEvent"]["tableStats"]
