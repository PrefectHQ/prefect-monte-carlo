"""
This is a module containing:
Montecarlo query_get_dbt_nodes* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_dbt_nodes.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_dbt_nodes(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: str = None,
    dbt_project_uuid: str = None,
    table_mcon: str = None,
    table_mcons: Iterable[str] = None,
    dbt_unique_ids: Iterable[str] = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: Filter by UUID of dbt node.
        dbt_project_uuid: Filter by UUID of dbt project.
        table_mcon: Filter by table MCON (deprecated, use tableMcons instead).
        table_mcons: Filter by list of table MCON.
        dbt_unique_ids: Filter by list of dbt node unique_id.
        before: None.
        after: None.
        first: None.
        last: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_dbt_nodes(
        **strip_kwargs(
            uuid=uuid,
            dbt_project_uuid=dbt_project_uuid,
            table_mcon=table_mcon,
            table_mcons=table_mcons,
            dbt_unique_ids=dbt_unique_ids,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    )

    op_stack = ("getDbtNodes",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDbtNodes"]


@task
async def query_get_dbt_nodes_edges(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: str = None,
    dbt_project_uuid: str = None,
    table_mcon: str = None,
    table_mcons: Iterable[str] = None,
    dbt_unique_ids: Iterable[str] = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Contains the nodes in this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: Filter by UUID of dbt node.
        dbt_project_uuid: Filter by UUID of dbt project.
        table_mcon: Filter by table MCON (deprecated, use
            tableMcons instead).
        table_mcons: Filter by list of table MCON.
        dbt_unique_ids: Filter by list of dbt node unique_id.
        before: None.
        after: None.
        first: None.
        last: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_dbt_nodes(
        **strip_kwargs(
            uuid=uuid,
            dbt_project_uuid=dbt_project_uuid,
            table_mcon=table_mcon,
            table_mcons=table_mcons,
            dbt_unique_ids=dbt_unique_ids,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).edges(**strip_kwargs())

    op_stack = (
        "getDbtNodes",
        "edges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDbtNodes"]["edges"]


@task
async def query_get_dbt_nodes_page_info(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: str = None,
    dbt_project_uuid: str = None,
    table_mcon: str = None,
    table_mcons: Iterable[str] = None,
    dbt_unique_ids: Iterable[str] = None,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Pagination data for this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: Filter by UUID of dbt node.
        dbt_project_uuid: Filter by UUID of dbt project.
        table_mcon: Filter by table MCON (deprecated, use
            tableMcons instead).
        table_mcons: Filter by list of table MCON.
        dbt_unique_ids: Filter by list of dbt node unique_id.
        before: None.
        after: None.
        first: None.
        last: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_dbt_nodes(
        **strip_kwargs(
            uuid=uuid,
            dbt_project_uuid=dbt_project_uuid,
            table_mcon=table_mcon,
            table_mcons=table_mcons,
            dbt_unique_ids=dbt_unique_ids,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).page_info(**strip_kwargs())

    op_stack = (
        "getDbtNodes",
        "pageInfo",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDbtNodes"]["pageInfo"]
