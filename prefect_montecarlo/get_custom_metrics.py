"""
This is a module containing:
Montecarlo query_get_custom_metrics* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_custom_metrics.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_custom_metrics(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    rule_uuid: datetime = None,
    start_time: datetime = None,
    end_time: datetime = None,
    first: int = 5000,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        rule_uuid: A custom rule UUID.
        start_time: Beginning of time range to retrieve metrics for.
        end_time: End of time range to retrieve metrics for.
        first: Limit of number of metrics retrieved.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_custom_metrics(
        **strip_kwargs(
            rule_uuid=rule_uuid,
            start_time=start_time,
            end_time=end_time,
            first=first,
        )
    )

    op_stack = ("getCustomMetrics",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getCustomMetrics"]


@task
async def query_get_custom_metrics_metrics(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    rule_uuid: datetime = None,
    start_time: datetime = None,
    end_time: datetime = None,
    first: int = 5000,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        rule_uuid: A custom rule UUID.
        start_time: Beginning of time range to retrieve
            metrics for.
        end_time: End of time range to retrieve metrics for.
        first: Limit of number of metrics retrieved.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_custom_metrics(
        **strip_kwargs(
            rule_uuid=rule_uuid,
            start_time=start_time,
            end_time=end_time,
            first=first,
        )
    ).metrics(**strip_kwargs())

    op_stack = (
        "getCustomMetrics",
        "metrics",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getCustomMetrics"]["metrics"]
