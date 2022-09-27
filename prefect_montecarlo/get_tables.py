"""
This is a module containing:
Montecarlo query_get_tables* tasks
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

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "get_tables.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_tables(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    search: str = None,
    status: Iterable[str] = None,
    domain_id: datetime = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    table_id: str = None,
    full_table_id: str = None,
    warehouse: str = None,
    discovered_time: datetime = None,
    friendly_name: str = None,
    description: str = None,
    location: str = None,
    project_name: str = None,
    dataset: str = None,
    table_type: str = None,
    is_encrypted: bool = None,
    created_time: datetime = None,
    last_modified: datetime = None,
    view_query: str = None,
    path: str = None,
    priority: int = None,
    tracked: bool = None,
    freshness_anomaly: bool = None,
    size_anomaly: bool = None,
    freshness_size_anomaly: bool = None,
    metric_anomaly: bool = None,
    dynamic_table: bool = None,
    is_deleted: bool = None,
    last_observed: datetime = None,
    data_provider: str = None,
    mcon: str = None,
    last_observed__gt: datetime = None,
    order_by: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Filter by a specific warehouse.
        search: Filter by partial asset names (e.g. dataset).
        status: Filter by table statuses.
        domain_id: Filter by domain UUID.
        before: None.
        after: None.
        first: None.
        last: None.
        table_id: None.
        full_table_id: None.
        warehouse: None.
        discovered_time: None.
        friendly_name: None.
        description: None.
        location: None.
        project_name: None.
        dataset: None.
        table_type: None.
        is_encrypted: None.
        created_time: None.
        last_modified: None.
        view_query: None.
        path: None.
        priority: None.
        tracked: None.
        freshness_anomaly: None.
        size_anomaly: None.
        freshness_size_anomaly: None.
        metric_anomaly: None.
        dynamic_table: None.
        is_deleted: None.
        last_observed: None.
        data_provider: None.
        mcon: None.
        last_observed__gt: None.
        order_by: Ordering.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_tables(
        **strip_kwargs(
            dw_id=dw_id,
            search=search,
            status=status,
            domain_id=domain_id,
            before=before,
            after=after,
            first=first,
            last=last,
            table_id=table_id,
            full_table_id=full_table_id,
            warehouse=warehouse,
            discovered_time=discovered_time,
            friendly_name=friendly_name,
            description=description,
            location=location,
            project_name=project_name,
            dataset=dataset,
            table_type=table_type,
            is_encrypted=is_encrypted,
            created_time=created_time,
            last_modified=last_modified,
            view_query=view_query,
            path=path,
            priority=priority,
            tracked=tracked,
            freshness_anomaly=freshness_anomaly,
            size_anomaly=size_anomaly,
            freshness_size_anomaly=freshness_size_anomaly,
            metric_anomaly=metric_anomaly,
            dynamic_table=dynamic_table,
            is_deleted=is_deleted,
            last_observed=last_observed,
            data_provider=data_provider,
            mcon=mcon,
            last_observed__gt=last_observed__gt,
            order_by=order_by,
        )
    )

    op_stack = ("getTables",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTables"]


@task
async def query_get_tables_edges(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    search: str = None,
    status: Iterable[str] = None,
    domain_id: datetime = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    table_id: str = None,
    full_table_id: str = None,
    warehouse: str = None,
    discovered_time: datetime = None,
    friendly_name: str = None,
    description: str = None,
    location: str = None,
    project_name: str = None,
    dataset: str = None,
    table_type: str = None,
    is_encrypted: bool = None,
    created_time: datetime = None,
    last_modified: datetime = None,
    view_query: str = None,
    path: str = None,
    priority: int = None,
    tracked: bool = None,
    freshness_anomaly: bool = None,
    size_anomaly: bool = None,
    freshness_size_anomaly: bool = None,
    metric_anomaly: bool = None,
    dynamic_table: bool = None,
    is_deleted: bool = None,
    last_observed: datetime = None,
    data_provider: str = None,
    mcon: str = None,
    last_observed__gt: datetime = None,
    order_by: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Contains the nodes in this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Filter by a specific warehouse.
        search: Filter by partial asset names (e.g. dataset).
        status: Filter by table statuses.
        domain_id: Filter by domain UUID.
        before: None.
        after: None.
        first: None.
        last: None.
        table_id: None.
        full_table_id: None.
        warehouse: None.
        discovered_time: None.
        friendly_name: None.
        description: None.
        location: None.
        project_name: None.
        dataset: None.
        table_type: None.
        is_encrypted: None.
        created_time: None.
        last_modified: None.
        view_query: None.
        path: None.
        priority: None.
        tracked: None.
        freshness_anomaly: None.
        size_anomaly: None.
        freshness_size_anomaly: None.
        metric_anomaly: None.
        dynamic_table: None.
        is_deleted: None.
        last_observed: None.
        data_provider: None.
        mcon: None.
        last_observed__gt: None.
        order_by: Ordering.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_tables(
        **strip_kwargs(
            dw_id=dw_id,
            search=search,
            status=status,
            domain_id=domain_id,
            before=before,
            after=after,
            first=first,
            last=last,
            table_id=table_id,
            full_table_id=full_table_id,
            warehouse=warehouse,
            discovered_time=discovered_time,
            friendly_name=friendly_name,
            description=description,
            location=location,
            project_name=project_name,
            dataset=dataset,
            table_type=table_type,
            is_encrypted=is_encrypted,
            created_time=created_time,
            last_modified=last_modified,
            view_query=view_query,
            path=path,
            priority=priority,
            tracked=tracked,
            freshness_anomaly=freshness_anomaly,
            size_anomaly=size_anomaly,
            freshness_size_anomaly=freshness_size_anomaly,
            metric_anomaly=metric_anomaly,
            dynamic_table=dynamic_table,
            is_deleted=is_deleted,
            last_observed=last_observed,
            data_provider=data_provider,
            mcon=mcon,
            last_observed__gt=last_observed__gt,
            order_by=order_by,
        )
    ).edges(**strip_kwargs())

    op_stack = (
        "getTables",
        "edges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTables"]["edges"]


@task
async def query_get_tables_page_info(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    search: str = None,
    status: Iterable[str] = None,
    domain_id: datetime = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    table_id: str = None,
    full_table_id: str = None,
    warehouse: str = None,
    discovered_time: datetime = None,
    friendly_name: str = None,
    description: str = None,
    location: str = None,
    project_name: str = None,
    dataset: str = None,
    table_type: str = None,
    is_encrypted: bool = None,
    created_time: datetime = None,
    last_modified: datetime = None,
    view_query: str = None,
    path: str = None,
    priority: int = None,
    tracked: bool = None,
    freshness_anomaly: bool = None,
    size_anomaly: bool = None,
    freshness_size_anomaly: bool = None,
    metric_anomaly: bool = None,
    dynamic_table: bool = None,
    is_deleted: bool = None,
    last_observed: datetime = None,
    data_provider: str = None,
    mcon: str = None,
    last_observed__gt: datetime = None,
    order_by: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Pagination data for this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Filter by a specific warehouse.
        search: Filter by partial asset names (e.g. dataset).
        status: Filter by table statuses.
        domain_id: Filter by domain UUID.
        before: None.
        after: None.
        first: None.
        last: None.
        table_id: None.
        full_table_id: None.
        warehouse: None.
        discovered_time: None.
        friendly_name: None.
        description: None.
        location: None.
        project_name: None.
        dataset: None.
        table_type: None.
        is_encrypted: None.
        created_time: None.
        last_modified: None.
        view_query: None.
        path: None.
        priority: None.
        tracked: None.
        freshness_anomaly: None.
        size_anomaly: None.
        freshness_size_anomaly: None.
        metric_anomaly: None.
        dynamic_table: None.
        is_deleted: None.
        last_observed: None.
        data_provider: None.
        mcon: None.
        last_observed__gt: None.
        order_by: Ordering.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_tables(
        **strip_kwargs(
            dw_id=dw_id,
            search=search,
            status=status,
            domain_id=domain_id,
            before=before,
            after=after,
            first=first,
            last=last,
            table_id=table_id,
            full_table_id=full_table_id,
            warehouse=warehouse,
            discovered_time=discovered_time,
            friendly_name=friendly_name,
            description=description,
            location=location,
            project_name=project_name,
            dataset=dataset,
            table_type=table_type,
            is_encrypted=is_encrypted,
            created_time=created_time,
            last_modified=last_modified,
            view_query=view_query,
            path=path,
            priority=priority,
            tracked=tracked,
            freshness_anomaly=freshness_anomaly,
            size_anomaly=size_anomaly,
            freshness_size_anomaly=freshness_size_anomaly,
            metric_anomaly=metric_anomaly,
            dynamic_table=dynamic_table,
            is_deleted=is_deleted,
            last_observed=last_observed,
            data_provider=data_provider,
            mcon=mcon,
            last_observed__gt=last_observed__gt,
            order_by=order_by,
        )
    ).page_info(**strip_kwargs())

    op_stack = (
        "getTables",
        "pageInfo",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTables"]["pageInfo"]
