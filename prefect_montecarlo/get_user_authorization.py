"""
This is a module containing:
Montecarlo query_get_user_authorization* tasks
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
    / "get_user_authorization.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_user_authorization(  # noqa
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
    op_selection = op.get_user_authorization(**strip_kwargs())

    op_stack = ("getUserAuthorization",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getUserAuthorization"]


@task
async def query_get_user_authorization_permissions(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Full list of permissions with resolved policy for the user.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_user_authorization(**strip_kwargs()).permissions(
        **strip_kwargs()
    )

    op_stack = (
        "getUserAuthorization",
        "permissions",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getUserAuthorization"]["permissions"]


@task
async def query_get_user_authorization_domain_restrictions(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Union of all discovered domain restrictions for the user. If empty, user has no
    restrictions. Note this list may not necessarily match the domain
    restrictions for a particular permission. This is simply a complete list of
    all discovered restrictions for the user--always check the restrictions on a
    permission against its own list of restrictions.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_user_authorization(**strip_kwargs()).domain_restrictions(
        **strip_kwargs()
    )

    op_stack = (
        "getUserAuthorization",
        "domainRestrictions",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getUserAuthorization"]["domainRestrictions"]
