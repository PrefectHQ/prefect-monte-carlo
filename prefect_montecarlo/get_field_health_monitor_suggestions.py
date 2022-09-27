"""
This is a module containing:
Montecarlo query_get_field_health_monitor_suggestions* tasks
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
    / "get_field_health_monitor_suggestions.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_field_health_monitor_suggestions(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    entities: Iterable[str] = None,
    order_by: str = None,
    domain_id: datetime = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        entities: Filter by associated entities (tables).
        order_by: Sorting of results.
        domain_id: Filter by domain UUID.
        before: None.
        after: None.
        first: None.
        last: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_field_health_monitor_suggestions(
        **strip_kwargs(
            entities=entities,
            order_by=order_by,
            domain_id=domain_id,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    )

    op_stack = ("getFieldHealthMonitorSuggestions",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getFieldHealthMonitorSuggestions"]


@task
async def query_get_field_health_monitor_suggestions_edges(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    entities: Iterable[str] = None,
    order_by: str = None,
    domain_id: datetime = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Contains the nodes in this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        entities: Filter by associated
            entities (tables).
        order_by: Sorting of results.
        domain_id: Filter by domain UUID.
        before: None.
        after: None.
        first: None.
        last: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_field_health_monitor_suggestions(
        **strip_kwargs(
            entities=entities,
            order_by=order_by,
            domain_id=domain_id,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).edges(**strip_kwargs())

    op_stack = (
        "getFieldHealthMonitorSuggestions",
        "edges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getFieldHealthMonitorSuggestions"]["edges"]


@task
async def query_get_field_health_monitor_suggestions_page_info(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    entities: Iterable[str] = None,
    order_by: str = None,
    domain_id: datetime = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Pagination data for this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        entities: Filter by associated
            entities (tables).
        order_by: Sorting of results.
        domain_id: Filter by domain UUID.
        before: None.
        after: None.
        first: None.
        last: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_field_health_monitor_suggestions(
        **strip_kwargs(
            entities=entities,
            order_by=order_by,
            domain_id=domain_id,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).page_info(**strip_kwargs())

    op_stack = (
        "getFieldHealthMonitorSuggestions",
        "pageInfo",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getFieldHealthMonitorSuggestions"]["pageInfo"]
