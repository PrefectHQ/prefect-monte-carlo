"""
This is a module containing:
Montecarlo query_get_table* tasks
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

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "get_table.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_table(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in. Required when using a
            fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is present.
        mcon: Mcon for table to get details for.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
        )
    )

    op_stack = ("getTable",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTable"]


@task
async def query_get_table_warehouse(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in. Required when
            using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Mcon for table to get details for.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
        )
    ).warehouse(**strip_kwargs())

    op_stack = (
        "getTable",
        "warehouse",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTable"]["warehouse"]


@task
async def query_get_table_table_stats(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Stats for the table.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in. Required when
            using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Mcon for table to get details for.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
        )
    ).table_stats(**strip_kwargs())

    op_stack = (
        "getTable",
        "tableStats",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTable"]["tableStats"]


@task
async def query_get_table_last_updates(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    start_time: datetime = None,
    end_time: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of table updates.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in. Required when
            using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Mcon for table to get details for.
        start_time: None.
        end_time: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
        )
    ).last_updates(
        **strip_kwargs(
            start_time=start_time,
            end_time=end_time,
        )
    )

    op_stack = (
        "getTable",
        "lastUpdates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTable"]["lastUpdates"]


@task
async def query_get_table_last_updates_v2(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    start_time: datetime = None,
    end_time: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of table updates.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in. Required when
            using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Mcon for table to get details for.
        start_time: None.
        end_time: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
        )
    ).last_updates_v2(
        **strip_kwargs(
            start_time=start_time,
            end_time=end_time,
        )
    )

    op_stack = (
        "getTable",
        "lastUpdatesV2",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTable"]["lastUpdatesV2"]


@task
async def query_get_table_total_row_counts(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    start_time: datetime = None,
    end_time: datetime = None,
    eliminate_gaps: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of total row count values for the table.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in. Required when
            using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Mcon for table to get details for.
        start_time: None.
        end_time: None.
        eliminate_gaps: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
        )
    ).total_row_counts(
        **strip_kwargs(
            start_time=start_time,
            end_time=end_time,
            eliminate_gaps=eliminate_gaps,
        )
    )

    op_stack = (
        "getTable",
        "totalRowCounts",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTable"]["totalRowCounts"]


@task
async def query_get_table_objects_deleted(  # noqa
    start_time: datetime,
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    end_time: datetime = None,
    granularity: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of latest objects deleted events, at most 10000 data points.

    Args:
        start_time: start time point of the metric.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in. Required when
            using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Mcon for table to get details for.
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
    op_selection = op.get_table(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
        )
    ).objects_deleted(
        **strip_kwargs(
            start_time=start_time,
            end_time=end_time,
            granularity=granularity,
        )
    )

    op_stack = (
        "getTable",
        "objectsDeleted",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTable"]["objectsDeleted"]


@task
async def query_get_table_total_byte_counts(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    start_time: datetime = None,
    end_time: datetime = None,
    eliminate_gaps: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of total byte count values for the table.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in. Required when
            using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Mcon for table to get details for.
        start_time: None.
        end_time: None.
        eliminate_gaps: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
        )
    ).total_byte_counts(
        **strip_kwargs(
            start_time=start_time,
            end_time=end_time,
            eliminate_gaps=eliminate_gaps,
        )
    )

    op_stack = (
        "getTable",
        "totalByteCounts",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTable"]["totalByteCounts"]


@task
async def query_get_table_write_throughput(  # noqa
    start_time: datetime,
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    end_time: datetime = None,
    granularity: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of latest write throughput in bytes, at most 10000 data points.

    Args:
        start_time: start time point of the metric.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in. Required when
            using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Mcon for table to get details for.
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
    op_selection = op.get_table(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
        )
    ).write_throughput(
        **strip_kwargs(
            start_time=start_time,
            end_time=end_time,
            granularity=granularity,
        )
    )

    op_stack = (
        "getTable",
        "writeThroughput",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTable"]["writeThroughput"]


@task
async def query_get_table_object_properties(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in. Required when
            using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Mcon for table to get details for.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
        )
    ).object_properties(**strip_kwargs())

    op_stack = (
        "getTable",
        "objectProperties",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTable"]["objectProperties"]


@task
async def query_get_table_table_capabilities(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Capabilities for the table.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in. Required when
            using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Mcon for table to get details for.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
        )
    ).table_capabilities(**strip_kwargs())

    op_stack = (
        "getTable",
        "tableCapabilities",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTable"]["tableCapabilities"]


@task
async def query_get_table_check_table_metrics_existence(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    full_table_id: str = None,
    mcon: str = None,
    metric_names: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of metric name and whether they exist or not on a table.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the table is contained in. Required when
            using a fullTableId.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Mcon for table to get details for.
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
    op_selection = op.get_table(
        **strip_kwargs(
            dw_id=dw_id,
            full_table_id=full_table_id,
            mcon=mcon,
        )
    ).check_table_metrics_existence(
        **strip_kwargs(
            metric_names=metric_names,
        )
    )

    op_stack = (
        "getTable",
        "checkTableMetricsExistence",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTable"]["checkTableMetricsExistence"]
