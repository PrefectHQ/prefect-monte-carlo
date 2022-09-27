"""
This is a module containing:
Montecarlo query_get_dbt_projects* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_dbt_projects.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_dbt_projects(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: str = None,
    project_name: str = None,
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
        uuid: None.
        project_name: None.
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
    op_selection = op.get_dbt_projects(
        **strip_kwargs(
            uuid=uuid,
            project_name=project_name,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    )

    op_stack = ("getDbtProjects",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDbtProjects"]


@task
async def query_get_dbt_projects_edges(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: str = None,
    project_name: str = None,
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
        uuid: None.
        project_name: None.
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
    op_selection = op.get_dbt_projects(
        **strip_kwargs(
            uuid=uuid,
            project_name=project_name,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).edges(**strip_kwargs())

    op_stack = (
        "getDbtProjects",
        "edges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDbtProjects"]["edges"]


@task
async def query_get_dbt_projects_page_info(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: str = None,
    project_name: str = None,
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
        uuid: None.
        project_name: None.
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
    op_selection = op.get_dbt_projects(
        **strip_kwargs(
            uuid=uuid,
            project_name=project_name,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).page_info(**strip_kwargs())

    op_stack = (
        "getDbtProjects",
        "pageInfo",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDbtProjects"]["pageInfo"]
