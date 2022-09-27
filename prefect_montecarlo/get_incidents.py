"""
This is a module containing:
Montecarlo query_get_incidents* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_incidents.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_incidents(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    incident_types: Iterable[str] = None,
    incident_sub_types: Iterable[graphql_schema.IncidentSubType] = None,
    event_types: Iterable[str] = None,
    event_states: Iterable[str] = None,
    start_time: datetime = None,
    end_time: datetime = None,
    incident_ids: Iterable[datetime] = None,
    include_feedback: Iterable[str] = None,
    exclude_feedback: Iterable[str] = None,
    projects: Iterable[str] = None,
    datasets: Iterable[str] = None,
    tables: Iterable[str] = None,
    full_table_ids: Iterable[str] = None,
    include_timeline_events: bool = None,
    include_anomaly_events: bool = None,
    domain_id: datetime = None,
    monitor_ids: Iterable[datetime] = None,
    reaction_types: Iterable[graphql_schema.IncidentReactionType] = None,
    rule_id: datetime = None,
    tag_key_values: Iterable[graphql_schema.TagPair] = None,
    tag_keys: Iterable[str] = None,
    min_event_count: int = None,
    max_event_count: int = None,
    contains_key_asset: bool = None,
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
        incident_types: Filter by type of incident (e.g. anomalies).
        incident_sub_types: Filter by incident sub type (e.g. freshness_anomaly).
        event_types: Filter by type of event as an incident can have multiple
            event types.
        event_states: Filter by the state individual events are in.
        start_time: Filter for incidents newer than this.
        end_time: Filter for incidents older than this.
        incident_ids: Filter for specific incidents.
        include_feedback: Filter by user feedback.
        exclude_feedback: Exclude by user feedback.
        projects: Filter by projects.
        datasets: Filter by datasets.
        tables: Filter by tables.
        full_table_ids: Filter by full table ids.
        include_timeline_events: Flag decides whether to include timeline events
            or not. By default it's false. If event_types field set,
            this will be ignored too.
        include_anomaly_events: Flag decides whether to include anomaly events
            or not. By default it's false. If event_types field set,
            this will be ignored too.
        domain_id: Filter by domain UUID.
        monitor_ids: Filter for specific monitors.
        reaction_types: Filter for specific reaction types.
        rule_id: Filter by custom rule UUID.
        tag_key_values: Filter by tag key values.
        tag_keys: Filter by tag keys.
        min_event_count: Filter to incidents with at least this many events.
        max_event_count: Filter to incidents with at most this many events.
        contains_key_asset: If true, filter to incidents containining a key
            asset.
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
    op_selection = op.get_incidents(
        **strip_kwargs(
            dw_id=dw_id,
            incident_types=incident_types,
            incident_sub_types=incident_sub_types,
            event_types=event_types,
            event_states=event_states,
            start_time=start_time,
            end_time=end_time,
            incident_ids=incident_ids,
            include_feedback=include_feedback,
            exclude_feedback=exclude_feedback,
            projects=projects,
            datasets=datasets,
            tables=tables,
            full_table_ids=full_table_ids,
            include_timeline_events=include_timeline_events,
            include_anomaly_events=include_anomaly_events,
            domain_id=domain_id,
            monitor_ids=monitor_ids,
            reaction_types=reaction_types,
            rule_id=rule_id,
            tag_key_values=tag_key_values,
            tag_keys=tag_keys,
            min_event_count=min_event_count,
            max_event_count=max_event_count,
            contains_key_asset=contains_key_asset,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    )

    op_stack = ("getIncidents",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidents"]


@task
async def query_get_incidents_edges(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    incident_types: Iterable[str] = None,
    incident_sub_types: Iterable[graphql_schema.IncidentSubType] = None,
    event_types: Iterable[str] = None,
    event_states: Iterable[str] = None,
    start_time: datetime = None,
    end_time: datetime = None,
    incident_ids: Iterable[datetime] = None,
    include_feedback: Iterable[str] = None,
    exclude_feedback: Iterable[str] = None,
    projects: Iterable[str] = None,
    datasets: Iterable[str] = None,
    tables: Iterable[str] = None,
    full_table_ids: Iterable[str] = None,
    include_timeline_events: bool = None,
    include_anomaly_events: bool = None,
    domain_id: datetime = None,
    monitor_ids: Iterable[datetime] = None,
    reaction_types: Iterable[graphql_schema.IncidentReactionType] = None,
    rule_id: datetime = None,
    tag_key_values: Iterable[graphql_schema.TagPair] = None,
    tag_keys: Iterable[str] = None,
    min_event_count: int = None,
    max_event_count: int = None,
    contains_key_asset: bool = None,
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
        incident_types: Filter by type of incident (e.g.
            anomalies).
        incident_sub_types: Filter by incident sub type (e.g.
            freshness_anomaly).
        event_types: Filter by type of event as an incident can
            have multiple event types.
        event_states: Filter by the state individual events are in.
        start_time: Filter for incidents newer than this.
        end_time: Filter for incidents older than this.
        incident_ids: Filter for specific incidents.
        include_feedback: Filter by user feedback.
        exclude_feedback: Exclude by user feedback.
        projects: Filter by projects.
        datasets: Filter by datasets.
        tables: Filter by tables.
        full_table_ids: Filter by full table ids.
        include_timeline_events: Flag decides whether to include
            timeline events or not. By default it's false. If
            event_types field set, this will be ignored too.
        include_anomaly_events: Flag decides whether to include
            anomaly events or not. By default it's false. If event_types
            field set, this will be ignored too.
        domain_id: Filter by domain UUID.
        monitor_ids: Filter for specific monitors.
        reaction_types: Filter for specific reaction types.
        rule_id: Filter by custom rule UUID.
        tag_key_values: Filter by tag key values.
        tag_keys: Filter by tag keys.
        min_event_count: Filter to incidents with at least this
            many events.
        max_event_count: Filter to incidents with at most this
            many events.
        contains_key_asset: If true, filter to incidents
            containining a key asset.
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
    op_selection = op.get_incidents(
        **strip_kwargs(
            dw_id=dw_id,
            incident_types=incident_types,
            incident_sub_types=incident_sub_types,
            event_types=event_types,
            event_states=event_states,
            start_time=start_time,
            end_time=end_time,
            incident_ids=incident_ids,
            include_feedback=include_feedback,
            exclude_feedback=exclude_feedback,
            projects=projects,
            datasets=datasets,
            tables=tables,
            full_table_ids=full_table_ids,
            include_timeline_events=include_timeline_events,
            include_anomaly_events=include_anomaly_events,
            domain_id=domain_id,
            monitor_ids=monitor_ids,
            reaction_types=reaction_types,
            rule_id=rule_id,
            tag_key_values=tag_key_values,
            tag_keys=tag_keys,
            min_event_count=min_event_count,
            max_event_count=max_event_count,
            contains_key_asset=contains_key_asset,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).edges(**strip_kwargs())

    op_stack = (
        "getIncidents",
        "edges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidents"]["edges"]


@task
async def query_get_incidents_page_info(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    incident_types: Iterable[str] = None,
    incident_sub_types: Iterable[graphql_schema.IncidentSubType] = None,
    event_types: Iterable[str] = None,
    event_states: Iterable[str] = None,
    start_time: datetime = None,
    end_time: datetime = None,
    incident_ids: Iterable[datetime] = None,
    include_feedback: Iterable[str] = None,
    exclude_feedback: Iterable[str] = None,
    projects: Iterable[str] = None,
    datasets: Iterable[str] = None,
    tables: Iterable[str] = None,
    full_table_ids: Iterable[str] = None,
    include_timeline_events: bool = None,
    include_anomaly_events: bool = None,
    domain_id: datetime = None,
    monitor_ids: Iterable[datetime] = None,
    reaction_types: Iterable[graphql_schema.IncidentReactionType] = None,
    rule_id: datetime = None,
    tag_key_values: Iterable[graphql_schema.TagPair] = None,
    tag_keys: Iterable[str] = None,
    min_event_count: int = None,
    max_event_count: int = None,
    contains_key_asset: bool = None,
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
        incident_types: Filter by type of incident (e.g.
            anomalies).
        incident_sub_types: Filter by incident sub type (e.g.
            freshness_anomaly).
        event_types: Filter by type of event as an incident can
            have multiple event types.
        event_states: Filter by the state individual events are in.
        start_time: Filter for incidents newer than this.
        end_time: Filter for incidents older than this.
        incident_ids: Filter for specific incidents.
        include_feedback: Filter by user feedback.
        exclude_feedback: Exclude by user feedback.
        projects: Filter by projects.
        datasets: Filter by datasets.
        tables: Filter by tables.
        full_table_ids: Filter by full table ids.
        include_timeline_events: Flag decides whether to include
            timeline events or not. By default it's false. If
            event_types field set, this will be ignored too.
        include_anomaly_events: Flag decides whether to include
            anomaly events or not. By default it's false. If event_types
            field set, this will be ignored too.
        domain_id: Filter by domain UUID.
        monitor_ids: Filter for specific monitors.
        reaction_types: Filter for specific reaction types.
        rule_id: Filter by custom rule UUID.
        tag_key_values: Filter by tag key values.
        tag_keys: Filter by tag keys.
        min_event_count: Filter to incidents with at least this
            many events.
        max_event_count: Filter to incidents with at most this
            many events.
        contains_key_asset: If true, filter to incidents
            containining a key asset.
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
    op_selection = op.get_incidents(
        **strip_kwargs(
            dw_id=dw_id,
            incident_types=incident_types,
            incident_sub_types=incident_sub_types,
            event_types=event_types,
            event_states=event_states,
            start_time=start_time,
            end_time=end_time,
            incident_ids=incident_ids,
            include_feedback=include_feedback,
            exclude_feedback=exclude_feedback,
            projects=projects,
            datasets=datasets,
            tables=tables,
            full_table_ids=full_table_ids,
            include_timeline_events=include_timeline_events,
            include_anomaly_events=include_anomaly_events,
            domain_id=domain_id,
            monitor_ids=monitor_ids,
            reaction_types=reaction_types,
            rule_id=rule_id,
            tag_key_values=tag_key_values,
            tag_keys=tag_keys,
            min_event_count=min_event_count,
            max_event_count=max_event_count,
            contains_key_asset=contains_key_asset,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).page_info(**strip_kwargs())

    op_stack = (
        "getIncidents",
        "pageInfo",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidents"]["pageInfo"]
