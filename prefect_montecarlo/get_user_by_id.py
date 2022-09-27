"""
This is a module containing:
Montecarlo query_get_user_by_id* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_user_by_id.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_user_by_id(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_user_by_id(**strip_kwargs())

    op_stack = ("getUserById",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getUserById"]


@task
async def query_get_user_by_id_auth(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    User's aggregate authorization policy.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_user_by_id(**strip_kwargs()).auth(**strip_kwargs())

    op_stack = (
        "getUserById",
        "auth",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getUserById"]["auth"]


@task
async def query_get_user_by_id_account(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_user_by_id(**strip_kwargs()).account(**strip_kwargs())

    op_stack = (
        "getUserById",
        "account",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getUserById"]["account"]


@task
async def query_get_user_by_id_lineage_nodes(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Who last updated the node.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_user_by_id(**strip_kwargs()).lineage_nodes(**strip_kwargs())

    op_stack = (
        "getUserById",
        "lineageNodes",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getUserById"]["lineageNodes"]


@task
async def query_get_user_by_id_lineage_edges(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Who last updated the edge.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_user_by_id(**strip_kwargs()).lineage_edges(**strip_kwargs())

    op_stack = (
        "getUserById",
        "lineageEdges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getUserById"]["lineageEdges"]


@task
async def query_get_user_by_id_slack_credentials_v2(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    User that installed the Slack app.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_user_by_id(**strip_kwargs()).slack_credentials_v2(
        **strip_kwargs()
    )

    op_stack = (
        "getUserById",
        "slackCredentialsV2",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getUserById"]["slackCredentialsV2"]


@task
async def query_get_user_by_id_lineage_block_patterns(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Who last updated the regexp.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_user_by_id(**strip_kwargs()).lineage_block_patterns(
        **strip_kwargs()
    )

    op_stack = (
        "getUserById",
        "lineageBlockPatterns",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getUserById"]["lineageBlockPatterns"]


@task
async def query_get_user_by_id_notification_settings_added(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Creator of the notification.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_user_by_id(**strip_kwargs()).notification_settings_added(
        **strip_kwargs()
    )

    op_stack = (
        "getUserById",
        "notificationSettingsAdded",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getUserById"]["notificationSettingsAdded"]


@task
async def query_get_user_by_id_notification_settings_modified(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    User who last updated this notification.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_user_by_id(**strip_kwargs()).notification_settings_modified(
        **strip_kwargs()
    )

    op_stack = (
        "getUserById",
        "notificationSettingsModified",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getUserById"]["notificationSettingsModified"]
