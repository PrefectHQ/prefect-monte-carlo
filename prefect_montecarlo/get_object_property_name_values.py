"""
This is a module containing:
Montecarlo query_get_object_property_name_values* tasks
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
    / "get_object_property_name_values.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_object_property_name_values(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    search_string: str = None,
    first: int = 100,
    offset: int = 0,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        search_string: None.
        first: None.
        offset: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_object_property_name_values(
        **strip_kwargs(
            search_string=search_string,
            first=first,
            offset=offset,
        )
    )

    op_stack = ("getObjectPropertyNameValues",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getObjectPropertyNameValues"]


@task
async def query_get_object_property_name_values_property_name_values(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    search_string: str = None,
    first: int = 100,
    offset: int = 0,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of unique object property name/value pairs.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        search_string: None.
        first: None.
        offset: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_object_property_name_values(
        **strip_kwargs(
            search_string=search_string,
            first=first,
            offset=offset,
        )
    ).property_name_values(**strip_kwargs())

    op_stack = (
        "getObjectPropertyNameValues",
        "propertyNameValues",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getObjectPropertyNameValues"]["propertyNameValues"]
