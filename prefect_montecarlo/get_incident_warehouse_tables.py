"""
This is a module containing:
Montecarlo query_get_incident_warehouse_tables* tasks
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
    / "get_incident_warehouse_tables.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_incident_warehouse_tables(  # noqa
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        incident_id: The incident UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_warehouse_tables(
        **strip_kwargs(
            incident_id=incident_id,
        )
    )

    op_stack = ("getIncidentWarehouseTables",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentWarehouseTables"]


@task
async def query_get_incident_warehouse_tables_warehouse(  # noqa
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        incident_id: The incident UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_warehouse_tables(
        **strip_kwargs(
            incident_id=incident_id,
        )
    ).warehouse(**strip_kwargs())

    op_stack = (
        "getIncidentWarehouseTables",
        "warehouse",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentWarehouseTables"]["warehouse"]


@task
async def query_get_incident_warehouse_tables_table_stats(  # noqa
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Stats for the table.

    Args:
        incident_id: The incident UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_warehouse_tables(
        **strip_kwargs(
            incident_id=incident_id,
        )
    ).table_stats(**strip_kwargs())

    op_stack = (
        "getIncidentWarehouseTables",
        "tableStats",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentWarehouseTables"]["tableStats"]


@task
async def query_get_incident_warehouse_tables_last_updates(  # noqa
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    start_time: datetime = None,
    end_time: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of table updates.

    Args:
        incident_id: The incident UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        start_time: None.
        end_time: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_warehouse_tables(
        **strip_kwargs(
            incident_id=incident_id,
        )
    ).last_updates(
        **strip_kwargs(
            start_time=start_time,
            end_time=end_time,
        )
    )

    op_stack = (
        "getIncidentWarehouseTables",
        "lastUpdates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentWarehouseTables"]["lastUpdates"]


@task
async def query_get_incident_warehouse_tables_last_updates_v2(  # noqa
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    start_time: datetime = None,
    end_time: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of table updates.

    Args:
        incident_id: The incident UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        start_time: None.
        end_time: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_warehouse_tables(
        **strip_kwargs(
            incident_id=incident_id,
        )
    ).last_updates_v2(
        **strip_kwargs(
            start_time=start_time,
            end_time=end_time,
        )
    )

    op_stack = (
        "getIncidentWarehouseTables",
        "lastUpdatesV2",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentWarehouseTables"]["lastUpdatesV2"]


@task
async def query_get_incident_warehouse_tables_total_row_counts(  # noqa
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    start_time: datetime = None,
    end_time: datetime = None,
    eliminate_gaps: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of total row count values for the table.

    Args:
        incident_id: The incident UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        start_time: None.
        end_time: None.
        eliminate_gaps: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_warehouse_tables(
        **strip_kwargs(
            incident_id=incident_id,
        )
    ).total_row_counts(
        **strip_kwargs(
            start_time=start_time,
            end_time=end_time,
            eliminate_gaps=eliminate_gaps,
        )
    )

    op_stack = (
        "getIncidentWarehouseTables",
        "totalRowCounts",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentWarehouseTables"]["totalRowCounts"]


@task
async def query_get_incident_warehouse_tables_objects_deleted(  # noqa
    incident_id: datetime,
    start_time: datetime,
    montecarlo_credentials: MontecarloCredentials,
    end_time: datetime = None,
    granularity: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of latest objects deleted events, at most 10000 data points.

    Args:
        incident_id: The incident UUID.
        start_time: start time point of the metric.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        end_time: end time point of the metric, if not
            specified, current timestamp will be used.
        granularity: Indicates the time interval to aggregate
            the result. By default it is 1h. We support xm(x minutes),
            xh(x hours), xd(x days).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_warehouse_tables(
        **strip_kwargs(
            incident_id=incident_id,
        )
    ).objects_deleted(
        **strip_kwargs(
            start_time=start_time,
            end_time=end_time,
            granularity=granularity,
        )
    )

    op_stack = (
        "getIncidentWarehouseTables",
        "objectsDeleted",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentWarehouseTables"]["objectsDeleted"]


@task
async def query_get_incident_warehouse_tables_total_byte_counts(  # noqa
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    start_time: datetime = None,
    end_time: datetime = None,
    eliminate_gaps: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of total byte count values for the table.

    Args:
        incident_id: The incident UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        start_time: None.
        end_time: None.
        eliminate_gaps: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_warehouse_tables(
        **strip_kwargs(
            incident_id=incident_id,
        )
    ).total_byte_counts(
        **strip_kwargs(
            start_time=start_time,
            end_time=end_time,
            eliminate_gaps=eliminate_gaps,
        )
    )

    op_stack = (
        "getIncidentWarehouseTables",
        "totalByteCounts",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentWarehouseTables"]["totalByteCounts"]


@task
async def query_get_incident_warehouse_tables_write_throughput(  # noqa
    incident_id: datetime,
    start_time: datetime,
    montecarlo_credentials: MontecarloCredentials,
    end_time: datetime = None,
    granularity: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of latest write throughput in bytes, at most 10000 data points.

    Args:
        incident_id: The incident UUID.
        start_time: start time point of the metric.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        end_time: end time point of the metric, if not
            specified, current timestamp will be used.
        granularity: Indicates the time interval to aggregate
            the result. By default it is 1h. We support xm(x minutes),
            xh(x hours), xd(x days).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_warehouse_tables(
        **strip_kwargs(
            incident_id=incident_id,
        )
    ).write_throughput(
        **strip_kwargs(
            start_time=start_time,
            end_time=end_time,
            granularity=granularity,
        )
    )

    op_stack = (
        "getIncidentWarehouseTables",
        "writeThroughput",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentWarehouseTables"]["writeThroughput"]


@task
async def query_get_incident_warehouse_tables_object_properties(  # noqa
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        incident_id: The incident UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_warehouse_tables(
        **strip_kwargs(
            incident_id=incident_id,
        )
    ).object_properties(**strip_kwargs())

    op_stack = (
        "getIncidentWarehouseTables",
        "objectProperties",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentWarehouseTables"]["objectProperties"]


@task
async def query_get_incident_warehouse_tables_table_capabilities(  # noqa
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Capabilities for the table.

    Args:
        incident_id: The incident UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_warehouse_tables(
        **strip_kwargs(
            incident_id=incident_id,
        )
    ).table_capabilities(**strip_kwargs())

    op_stack = (
        "getIncidentWarehouseTables",
        "tableCapabilities",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentWarehouseTables"]["tableCapabilities"]


@task
async def query_get_incident_warehouse_tables_check_table_metrics_existence(  # noqa
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    metric_names: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of metric name and whether they exist or not on a table.

    Args:
        incident_id: The incident UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        metric_names: list of metric names to
            check whether they exist or not. If not specified, we will
            check total_byte_count, total_row_count, write_throughput
            and objects_deleted for now.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_incident_warehouse_tables(
        **strip_kwargs(
            incident_id=incident_id,
        )
    ).check_table_metrics_existence(
        **strip_kwargs(
            metric_names=metric_names,
        )
    )

    op_stack = (
        "getIncidentWarehouseTables",
        "checkTableMetricsExistence",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getIncidentWarehouseTables"]["checkTableMetricsExistence"]
