"""
This is a module containing:
Montecarlo query_get_comments_for_monitor_incidents* tasks
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
    / "get_comments_for_monitor_incidents.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_comments_for_monitor_incidents(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    monitor_uuids: Iterable[datetime] = None,
    start_time: datetime = None,
    end_time: datetime = None,
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
        monitor_uuids: Monitor uuids.
        start_time: Filter for comments newer than this.
        end_time: Filter for comments older than this.
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
    op_selection = op.get_comments_for_monitor_incidents(
        **strip_kwargs(
            monitor_uuids=monitor_uuids,
            start_time=start_time,
            end_time=end_time,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    )

    op_stack = ("getCommentsForMonitorIncidents",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getCommentsForMonitorIncidents"]


@task
async def query_get_comments_for_monitor_incidents_edges(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    monitor_uuids: Iterable[datetime] = None,
    start_time: datetime = None,
    end_time: datetime = None,
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
        monitor_uuids: Monitor uuids.
        start_time: Filter for comments newer
            than this.
        end_time: Filter for comments older
            than this.
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
    op_selection = op.get_comments_for_monitor_incidents(
        **strip_kwargs(
            monitor_uuids=monitor_uuids,
            start_time=start_time,
            end_time=end_time,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).edges(**strip_kwargs())

    op_stack = (
        "getCommentsForMonitorIncidents",
        "edges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getCommentsForMonitorIncidents"]["edges"]


@task
async def query_get_comments_for_monitor_incidents_page_info(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    monitor_uuids: Iterable[datetime] = None,
    start_time: datetime = None,
    end_time: datetime = None,
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
        monitor_uuids: Monitor uuids.
        start_time: Filter for comments newer
            than this.
        end_time: Filter for comments older
            than this.
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
    op_selection = op.get_comments_for_monitor_incidents(
        **strip_kwargs(
            monitor_uuids=monitor_uuids,
            start_time=start_time,
            end_time=end_time,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).page_info(**strip_kwargs())

    op_stack = (
        "getCommentsForMonitorIncidents",
        "pageInfo",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getCommentsForMonitorIncidents"]["pageInfo"]
