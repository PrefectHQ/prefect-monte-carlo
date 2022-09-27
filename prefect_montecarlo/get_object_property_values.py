"""
This is a module containing:
Montecarlo query_get_object_property_values* tasks
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
    / "get_object_property_values.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_object_property_values(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    limit: int = 100,
    offset: int = 0,
    property_name: str = None,
    search_string: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        limit: None.
        offset: None.
        property_name: Filter by property name.
        search_string: Filter property values by search string.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_object_property_values(
        **strip_kwargs(
            limit=limit,
            offset=offset,
            property_name=property_name,
            search_string=search_string,
        )
    )

    op_stack = ("getObjectPropertyValues",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getObjectPropertyValues"]
