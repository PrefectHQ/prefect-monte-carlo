"""
This is a module containing:
Montecarlo query_get_datasets* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_datasets.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_datasets(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    search: str = None,
    domain_id: datetime = None,
    include_table_count: bool = False,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    dataset: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Filter by a specific warehouse.
        search: Filter by a dataset.
        domain_id: Filter by domain UUID.
        include_table_count: Include table count for each dataset.
        before: None.
        after: None.
        first: None.
        last: None.
        dataset: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_datasets(
        **strip_kwargs(
            dw_id=dw_id,
            search=search,
            domain_id=domain_id,
            include_table_count=include_table_count,
            before=before,
            after=after,
            first=first,
            last=last,
            dataset=dataset,
        )
    )

    op_stack = ("getDatasets",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDatasets"]


@task
async def query_get_datasets_edges(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    search: str = None,
    domain_id: datetime = None,
    include_table_count: bool = False,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    dataset: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Contains the nodes in this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Filter by a specific warehouse.
        search: Filter by a dataset.
        domain_id: Filter by domain UUID.
        include_table_count: Include table count for each dataset.
        before: None.
        after: None.
        first: None.
        last: None.
        dataset: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_datasets(
        **strip_kwargs(
            dw_id=dw_id,
            search=search,
            domain_id=domain_id,
            include_table_count=include_table_count,
            before=before,
            after=after,
            first=first,
            last=last,
            dataset=dataset,
        )
    ).edges(**strip_kwargs())

    op_stack = (
        "getDatasets",
        "edges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDatasets"]["edges"]


@task
async def query_get_datasets_page_info(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    search: str = None,
    domain_id: datetime = None,
    include_table_count: bool = False,
    before: str = None,
    after: str = None,
    first: int = None,
    last: int = None,
    dataset: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Pagination data for this connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Filter by a specific warehouse.
        search: Filter by a dataset.
        domain_id: Filter by domain UUID.
        include_table_count: Include table count for each dataset.
        before: None.
        after: None.
        first: None.
        last: None.
        dataset: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_datasets(
        **strip_kwargs(
            dw_id=dw_id,
            search=search,
            domain_id=domain_id,
            include_table_count=include_table_count,
            before=before,
            after=after,
            first=first,
            last=last,
            dataset=dataset,
        )
    ).page_info(**strip_kwargs())

    op_stack = (
        "getDatasets",
        "pageInfo",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDatasets"]["pageInfo"]
