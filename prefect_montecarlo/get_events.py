"""
This is a module containing:
Montecarlo query_get_events* tasks
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

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "get_events.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_events(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    event_type: str = None,
    event_types: Iterable[str] = None,
    dataset: str = None,
    tables_older_than_days: int = None,
    event_states: Iterable[str] = None,
    exclude_state: str = None,
    start_time: datetime = None,
    end_time: datetime = None,
    incident_id: datetime = None,
    include_timeline_events: bool = None,
    include_anomaly_events: bool = None,
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
        dw_id: Filter by a specific warehouse.
        full_table_id: Filter by the full table id (e.g. project:dataset.table).
        event_type: Filter by the type of event.
        event_types: Filter by a list of types.
        dataset: Filter by the dataset.
        tables_older_than_days: Filter for events based on table age.
        event_states: Filter by a list of states.
        exclude_state: Exclude a specific state.
        start_time: Filter for events newer than this.
        end_time: Filter for events older than this.
        incident_id: Filter by incident (grouping of related events).
        include_timeline_events: Flag that decides whether to include incident
            timeline related events. If event_types specified, this will
            be ignored.
        include_anomaly_events: Flag that decides whether to include anomaly
            timeline related events. If event_types sepcified, this will
            be ignored.
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
    op_selection = op.get_events(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            event_type=event_type,
            event_types=event_types,
            dataset=dataset,
            tables_older_than_days=tables_older_than_days,
            event_states=event_states,
            exclude_state=exclude_state,
            start_time=start_time,
            end_time=end_time,
            incident_id=incident_id,
            include_timeline_events=include_timeline_events,
            include_anomaly_events=include_anomaly_events,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    )

    op_stack = ("getEvents",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getEvents"]


@task
async def query_get_events_edges(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    event_type: str = None,
    event_types: Iterable[str] = None,
    dataset: str = None,
    tables_older_than_days: int = None,
    event_states: Iterable[str] = None,
    exclude_state: str = None,
    start_time: datetime = None,
    end_time: datetime = None,
    incident_id: datetime = None,
    include_timeline_events: bool = None,
    include_anomaly_events: bool = None,
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
        dw_id: Filter by a specific warehouse.
        full_table_id: Filter by the full table id (e.g.
            project:dataset.table).
        event_type: Filter by the type of event.
        event_types: Filter by a list of types.
        dataset: Filter by the dataset.
        tables_older_than_days: Filter for events based on table age.
        event_states: Filter by a list of states.
        exclude_state: Exclude a specific state.
        start_time: Filter for events newer than this.
        end_time: Filter for events older than this.
        incident_id: Filter by incident (grouping of related events).
        include_timeline_events: Flag that decides whether to include
            incident timeline related events. If event_types specified,
            this will be ignored.
        include_anomaly_events: Flag that decides whether to include
            anomaly timeline related events. If event_types sepcified,
            this will be ignored.
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
    op_selection = op.get_events(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            event_type=event_type,
            event_types=event_types,
            dataset=dataset,
            tables_older_than_days=tables_older_than_days,
            event_states=event_states,
            exclude_state=exclude_state,
            start_time=start_time,
            end_time=end_time,
            incident_id=incident_id,
            include_timeline_events=include_timeline_events,
            include_anomaly_events=include_anomaly_events,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).edges(**strip_kwargs())

    op_stack = (
        "getEvents",
        "edges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getEvents"]["edges"]


@task
async def query_get_events_page_info(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    event_type: str = None,
    event_types: Iterable[str] = None,
    dataset: str = None,
    tables_older_than_days: int = None,
    event_states: Iterable[str] = None,
    exclude_state: str = None,
    start_time: datetime = None,
    end_time: datetime = None,
    incident_id: datetime = None,
    include_timeline_events: bool = None,
    include_anomaly_events: bool = None,
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
        dw_id: Filter by a specific warehouse.
        full_table_id: Filter by the full table id (e.g.
            project:dataset.table).
        event_type: Filter by the type of event.
        event_types: Filter by a list of types.
        dataset: Filter by the dataset.
        tables_older_than_days: Filter for events based on table age.
        event_states: Filter by a list of states.
        exclude_state: Exclude a specific state.
        start_time: Filter for events newer than this.
        end_time: Filter for events older than this.
        incident_id: Filter by incident (grouping of related events).
        include_timeline_events: Flag that decides whether to include
            incident timeline related events. If event_types specified,
            this will be ignored.
        include_anomaly_events: Flag that decides whether to include
            anomaly timeline related events. If event_types sepcified,
            this will be ignored.
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
    op_selection = op.get_events(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            event_type=event_type,
            event_types=event_types,
            dataset=dataset,
            tables_older_than_days=tables_older_than_days,
            event_states=event_states,
            exclude_state=exclude_state,
            start_time=start_time,
            end_time=end_time,
            incident_id=incident_id,
            include_timeline_events=include_timeline_events,
            include_anomaly_events=include_anomaly_events,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).page_info(**strip_kwargs())

    op_stack = (
        "getEvents",
        "pageInfo",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getEvents"]["pageInfo"]
