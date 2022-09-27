"""
This is a module containing:
Montecarlo query_search* tasks
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

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "search.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_search(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    object_types: Iterable[str] = None,
    ignore_object_types: Iterable[str] = None,
    query: str = None,
    offset: int = 0,
    limit: int = 50,
    full_results: bool = True,
    operator: str = "OR",
    mcon: str = None,
    parent_mcon: str = None,
    domain_id: datetime = None,
    tags_only: bool = False,
    include_facet_types: Iterable[graphql_schema.FacetType] = None,
    tags: Iterable[str] = None,
    tag_name_query: str = None,
    tag_value_query: str = None,
    resource_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        object_types: Filter by object type (e.g. table, view, etc.).
        ignore_object_types: Filter out by object type.
        query: Entity to search for.
        offset: Offset when paging.
        limit: Max results.
        full_results: Full search mode, used to search all available fields, not
            just display_name.
        operator: Search operator to use, either OR or AND (DEPRECATED).
        mcon: Filter on mcon.
        parent_mcon: Filter on parent_mcon.
        domain_id: Filter by domain UUID.
        tags_only: Search only tags and descriptions (no display_name).
        include_facet_types: Facet types to include (tags, tag_names,
            tag_values).
        tags: Filter by tags.
        tag_name_query: Query tag names (DEPRECATED).
        tag_value_query: Query tag values (DEPRECATED).
        resource_ids: Filter by resource ID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.search(
        **strip_kwargs(
            object_types=object_types,
            ignore_object_types=ignore_object_types,
            query=query,
            offset=offset,
            limit=limit,
            full_results=full_results,
            operator=operator,
            mcon=mcon,
            parent_mcon=parent_mcon,
            domain_id=domain_id,
            tags_only=tags_only,
            include_facet_types=include_facet_types,
            tags=tags,
            tag_name_query=tag_name_query,
            tag_value_query=tag_value_query,
            resource_ids=resource_ids,
        )
    )

    op_stack = ("search",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["search"]


@task
async def query_search_results(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    object_types: Iterable[str] = None,
    ignore_object_types: Iterable[str] = None,
    query: str = None,
    offset: int = 0,
    limit: int = 50,
    full_results: bool = True,
    operator: str = "OR",
    mcon: str = None,
    parent_mcon: str = None,
    domain_id: datetime = None,
    tags_only: bool = False,
    include_facet_types: Iterable[graphql_schema.FacetType] = None,
    tags: Iterable[str] = None,
    tag_name_query: str = None,
    tag_value_query: str = None,
    resource_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of matching results.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        object_types: Filter by object type (e.g. table, view, etc.).
        ignore_object_types: Filter out by object type.
        query: Entity to search for.
        offset: Offset when paging.
        limit: Max results.
        full_results: Full search mode, used to search all available
            fields, not just display_name.
        operator: Search operator to use, either OR or AND (DEPRECATED).
        mcon: Filter on mcon.
        parent_mcon: Filter on parent_mcon.
        domain_id: Filter by domain UUID.
        tags_only: Search only tags and descriptions (no display_name).
        include_facet_types: Facet types to include (tags, tag_names,
            tag_values).
        tags: Filter by tags.
        tag_name_query: Query tag names (DEPRECATED).
        tag_value_query: Query tag values (DEPRECATED).
        resource_ids: Filter by resource ID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.search(
        **strip_kwargs(
            object_types=object_types,
            ignore_object_types=ignore_object_types,
            query=query,
            offset=offset,
            limit=limit,
            full_results=full_results,
            operator=operator,
            mcon=mcon,
            parent_mcon=parent_mcon,
            domain_id=domain_id,
            tags_only=tags_only,
            include_facet_types=include_facet_types,
            tags=tags,
            tag_name_query=tag_name_query,
            tag_value_query=tag_value_query,
            resource_ids=resource_ids,
        )
    ).results(**strip_kwargs())

    op_stack = (
        "search",
        "results",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["search"]["results"]


@task
async def query_search_facet_results(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    object_types: Iterable[str] = None,
    ignore_object_types: Iterable[str] = None,
    query: str = None,
    offset: int = 0,
    limit: int = 50,
    full_results: bool = True,
    operator: str = "OR",
    mcon: str = None,
    parent_mcon: str = None,
    domain_id: datetime = None,
    tags_only: bool = False,
    include_facet_types: Iterable[graphql_schema.FacetType] = None,
    tags: Iterable[str] = None,
    tag_name_query: str = None,
    tag_value_query: str = None,
    resource_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Facet results.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        object_types: Filter by object type (e.g. table, view, etc.).
        ignore_object_types: Filter out by object type.
        query: Entity to search for.
        offset: Offset when paging.
        limit: Max results.
        full_results: Full search mode, used to search all available
            fields, not just display_name.
        operator: Search operator to use, either OR or AND (DEPRECATED).
        mcon: Filter on mcon.
        parent_mcon: Filter on parent_mcon.
        domain_id: Filter by domain UUID.
        tags_only: Search only tags and descriptions (no display_name).
        include_facet_types: Facet types to include (tags, tag_names,
            tag_values).
        tags: Filter by tags.
        tag_name_query: Query tag names (DEPRECATED).
        tag_value_query: Query tag values (DEPRECATED).
        resource_ids: Filter by resource ID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.search(
        **strip_kwargs(
            object_types=object_types,
            ignore_object_types=ignore_object_types,
            query=query,
            offset=offset,
            limit=limit,
            full_results=full_results,
            operator=operator,
            mcon=mcon,
            parent_mcon=parent_mcon,
            domain_id=domain_id,
            tags_only=tags_only,
            include_facet_types=include_facet_types,
            tags=tags,
            tag_name_query=tag_name_query,
            tag_value_query=tag_value_query,
            resource_ids=resource_ids,
        )
    ).facet_results(**strip_kwargs())

    op_stack = (
        "search",
        "facetResults",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["search"]["facetResults"]
