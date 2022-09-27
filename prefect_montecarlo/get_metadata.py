"""
This is a module containing:
Montecarlo query_get_metadata* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_metadata.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_metadata(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    mcons: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        mcons: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_metadata(
        **strip_kwargs(
            mcons=mcons,
        )
    )

    op_stack = ("getMetadata",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMetadata"]


@task
async def query_get_metadata_bi_metadata(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    mcons: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        mcons: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_metadata(
        **strip_kwargs(
            mcons=mcons,
        )
    ).bi_metadata(**strip_kwargs())

    op_stack = (
        "getMetadata",
        "biMetadata",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMetadata"]["biMetadata"]


@task
async def query_get_metadata_properties(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    mcons: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        mcons: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_metadata(
        **strip_kwargs(
            mcons=mcons,
        )
    ).properties(**strip_kwargs())

    op_stack = (
        "getMetadata",
        "properties",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMetadata"]["properties"]


@task
async def query_get_metadata_field_metadata(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    mcons: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        mcons: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_metadata(
        **strip_kwargs(
            mcons=mcons,
        )
    ).field_metadata(**strip_kwargs())

    op_stack = (
        "getMetadata",
        "fieldMetadata",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMetadata"]["fieldMetadata"]


@task
async def query_get_metadata_table_metadata(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    mcons: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        mcons: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_metadata(
        **strip_kwargs(
            mcons=mcons,
        )
    ).table_metadata(**strip_kwargs())

    op_stack = (
        "getMetadata",
        "tableMetadata",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getMetadata"]["tableMetadata"]
