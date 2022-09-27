"""
This is a module containing:
Montecarlo query_get_custom_rules* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_custom_rules.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_custom_rules(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    rule_type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        before: None.
        after: None.
        first: None.
        last: None.
        rule_type: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_custom_rules(
        **strip_kwargs(
            before=before,
            after=after,
            first=first,
            last=last,
            rule_type=rule_type,
        )
    )

    op_stack = ("getCustomRules",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getCustomRules"]


@task
async def query_get_custom_rules_edges(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    rule_type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Contains the nodes in this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        before: None.
        after: None.
        first: None.
        last: None.
        rule_type: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_custom_rules(
        **strip_kwargs(
            before=before,
            after=after,
            first=first,
            last=last,
            rule_type=rule_type,
        )
    ).edges(**strip_kwargs())

    op_stack = (
        "getCustomRules",
        "edges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getCustomRules"]["edges"]


@task
async def query_get_custom_rules_page_info(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    rule_type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Pagination data for this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        before: None.
        after: None.
        first: None.
        last: None.
        rule_type: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_custom_rules(
        **strip_kwargs(
            before=before,
            after=after,
            first=first,
            last=last,
            rule_type=rule_type,
        )
    ).page_info(**strip_kwargs())

    op_stack = (
        "getCustomRules",
        "pageInfo",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getCustomRules"]["pageInfo"]
