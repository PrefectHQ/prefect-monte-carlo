"""
This is a module containing:
Montecarlo query_get_slack_oauth_url* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_slack_oauth_url.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_slack_oauth_url(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    slack_app_type: graphql_schema.SlackAppType = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        slack_app_type: Slack app type.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_slack_oauth_url(
        **strip_kwargs(
            slack_app_type=slack_app_type,
        )
    )

    op_stack = ("getSlackOauthUrl",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getSlackOauthUrl"]
