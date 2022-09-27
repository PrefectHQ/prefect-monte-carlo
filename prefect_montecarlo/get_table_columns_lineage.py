"""
This is a module containing:
Montecarlo query_get_table_columns_lineage* tasks
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
    / "get_table_columns_lineage.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_table_columns_lineage(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    mcon: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        mcon: Destination table mcon.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table_columns_lineage(
        **strip_kwargs(
            mcon=mcon,
        )
    )

    op_stack = ("getTableColumnsLineage",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTableColumnsLineage"]


@task
async def query_get_table_columns_lineage_columns_lineage(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    mcon: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Lineage of the columns in the table.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        mcon: Destination table mcon.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table_columns_lineage(
        **strip_kwargs(
            mcon=mcon,
        )
    ).columns_lineage(**strip_kwargs())

    op_stack = (
        "getTableColumnsLineage",
        "columnsLineage",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTableColumnsLineage"]["columnsLineage"]


@task
async def query_get_table_columns_lineage_non_selected_source_columns(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    mcon: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Other columns used in conditions for the current table.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        mcon: Destination table mcon.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_table_columns_lineage(
        **strip_kwargs(
            mcon=mcon,
        )
    ).non_selected_source_columns(**strip_kwargs())

    op_stack = (
        "getTableColumnsLineage",
        "nonSelectedSourceColumns",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getTableColumnsLineage"]["nonSelectedSourceColumns"]
