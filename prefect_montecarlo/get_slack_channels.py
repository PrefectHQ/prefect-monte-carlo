"""
This is a module containing:
Montecarlo query_get_slack_channels* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_slack_channels.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_slack_channels(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    exclude_archived: bool = None,
    ignore_cached: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        exclude_archived: Specify whether to include archived Slack Channels.
        ignore_cached: Specify whether to ignore the cached versions and attempt
            to pull directly from Slack API.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_slack_channels(
        **strip_kwargs(
            exclude_archived=exclude_archived,
            ignore_cached=ignore_cached,
        )
    )

    op_stack = ("getSlackChannels",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getSlackChannels"]


@task
async def query_get_slack_channels_channels(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    exclude_archived: bool = None,
    ignore_cached: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        exclude_archived: Specify whether to include archived
            Slack Channels.
        ignore_cached: Specify whether to ignore the cached
            versions and attempt to pull directly from Slack API.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_slack_channels(
        **strip_kwargs(
            exclude_archived=exclude_archived,
            ignore_cached=ignore_cached,
        )
    ).channels(**strip_kwargs())

    op_stack = (
        "getSlackChannels",
        "channels",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getSlackChannels"]["channels"]
