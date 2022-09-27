"""
This is a module containing:
Montecarlo query_get_resource* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_resource.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_resource(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    name: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: The resource id.
        name: The resource name.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_resource(
        **strip_kwargs(
            uuid=uuid,
            name=name,
        )
    )

    op_stack = ("getResource",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getResource"]


@task
async def query_get_resource_account(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    name: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Customer account.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: The resource id.
        name: The resource name.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_resource(
        **strip_kwargs(
            uuid=uuid,
            name=name,
        )
    ).account(**strip_kwargs())

    op_stack = (
        "getResource",
        "account",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getResource"]["account"]


@task
async def query_get_resource_last_update_user(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    name: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Who last updated the resource.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: The resource id.
        name: The resource name.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_resource(
        **strip_kwargs(
            uuid=uuid,
            name=name,
        )
    ).last_update_user(**strip_kwargs())

    op_stack = (
        "getResource",
        "lastUpdateUser",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getResource"]["lastUpdateUser"]
