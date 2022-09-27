"""
This is a module containing:
Montecarlo query_get_job_execution_history_logs* tasks
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

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
    / "get_job_execution_history_logs.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_job_execution_history_logs(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    job_schedule_uuid: str = None,
    monitor_uuid: str = None,
    custom_rule_uuid: str = None,
    history_days: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        job_schedule_uuid: UUID of job schedule.
        monitor_uuid: UUID of monitor.
        custom_rule_uuid: UUID of custom rule.
        history_days: Number of days back.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_job_execution_history_logs(
        **strip_kwargs(
            job_schedule_uuid=job_schedule_uuid,
            monitor_uuid=monitor_uuid,
            custom_rule_uuid=custom_rule_uuid,
            history_days=history_days,
        )
    )

    op_stack = ("getJobExecutionHistoryLogs",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getJobExecutionHistoryLogs"]


@task
async def query_get_job_execution_history_logs_exceptions_detail(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    job_schedule_uuid: str = None,
    monitor_uuid: str = None,
    custom_rule_uuid: str = None,
    history_days: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Exceptions that were captured during this job execution.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        job_schedule_uuid: UUID of job schedule.
        monitor_uuid: UUID of monitor.
        custom_rule_uuid: UUID of custom rule.
        history_days: Number of days back.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_job_execution_history_logs(
        **strip_kwargs(
            job_schedule_uuid=job_schedule_uuid,
            monitor_uuid=monitor_uuid,
            custom_rule_uuid=custom_rule_uuid,
            history_days=history_days,
        )
    ).exceptions_detail(**strip_kwargs())

    op_stack = (
        "getJobExecutionHistoryLogs",
        "exceptionsDetail",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getJobExecutionHistoryLogs"]["exceptionsDetail"]
