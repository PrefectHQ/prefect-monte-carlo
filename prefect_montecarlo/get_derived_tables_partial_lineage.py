"""
This is a module containing:
Montecarlo query_get_derived_tables_partial_lineage* tasks
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
    / "get_derived_tables_partial_lineage.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_derived_tables_partial_lineage(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    mcon: str = None,
    column: str = None,
    cursor: str = None,
    page_size: int = 20,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        mcon: source table mcon.
        column: source column.
        cursor: cursor for getting the next page.
        page_size: number of derived tables to return in a call.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_derived_tables_partial_lineage(
        **strip_kwargs(
            mcon=mcon,
            column=column,
            cursor=cursor,
            page_size=page_size,
        )
    )

    op_stack = ("getDerivedTablesPartialLineage",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDerivedTablesPartialLineage"]


@task
async def query_get_derived_tables_partial_lineage_destinations(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    mcon: str = None,
    column: str = None,
    cursor: str = None,
    page_size: int = 20,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Derived tables and their columns that are influenced by the source col.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        mcon: source table mcon.
        column: source column.
        cursor: cursor for getting the next
            page.
        page_size: number of derived tables
            to return in a call.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_derived_tables_partial_lineage(
        **strip_kwargs(
            mcon=mcon,
            column=column,
            cursor=cursor,
            page_size=page_size,
        )
    ).destinations(**strip_kwargs())

    op_stack = (
        "getDerivedTablesPartialLineage",
        "destinations",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDerivedTablesPartialLineage"]["destinations"]
