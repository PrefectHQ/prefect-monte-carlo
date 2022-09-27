"""
This is a module containing:
Montecarlo query_get_all_user_defined_monitors_v2* tasks
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
    Path(__file__).parent.resolve()
    / "configs"
    / "query"
    / "get_all_user_defined_monitors_v2.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_all_user_defined_monitors_v2(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    user_defined_monitor_types: Iterable[str] = None,
    created_by: Iterable[str] = None,
    order_by: str = None,
    entities: Iterable[str] = None,
    description_field_or_table: Iterable[str] = None,
    domain_id: datetime = None,
    is_template_managed: bool = None,
    namespace: Iterable[str] = None,
    rule_name: Iterable[str] = None,
    search: Iterable[str] = None,
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
        user_defined_monitor_types: Filter by monitor type.
        created_by: Filter by creator.
        order_by: Sorting of results.
        entities: Filter by associated entities (tables).
        description_field_or_table: Match text on rule description, table, or
            field.
        domain_id: Filter by domain UUID.
        is_template_managed: Filter monitors created by code.
        namespace: Filter by namespace -> used in monitors created by code.
        rule_name: Filter by rule_name -> used in monitors created by code.
        search: Filter by: description, field, table, rule name, creator,
            namespace.
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
    op_selection = op.get_all_user_defined_monitors_v2(
        **strip_kwargs(
            user_defined_monitor_types=user_defined_monitor_types,
            created_by=created_by,
            order_by=order_by,
            entities=entities,
            description_field_or_table=description_field_or_table,
            domain_id=domain_id,
            is_template_managed=is_template_managed,
            namespace=namespace,
            rule_name=rule_name,
            search=search,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    )

    op_stack = ("getAllUserDefinedMonitorsV2",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getAllUserDefinedMonitorsV2"]


@task
async def query_get_all_user_defined_monitors_v2_edges(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    user_defined_monitor_types: Iterable[str] = None,
    created_by: Iterable[str] = None,
    order_by: str = None,
    entities: Iterable[str] = None,
    description_field_or_table: Iterable[str] = None,
    domain_id: datetime = None,
    is_template_managed: bool = None,
    namespace: Iterable[str] = None,
    rule_name: Iterable[str] = None,
    search: Iterable[str] = None,
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
        user_defined_monitor_types: Filter by
            monitor type.
        created_by: Filter by creator.
        order_by: Sorting of results.
        entities: Filter by associated entities
            (tables).
        description_field_or_table: Match text
            on rule description, table, or field.
        domain_id: Filter by domain UUID.
        is_template_managed: Filter monitors
            created by code.
        namespace: Filter by namespace -> used
            in monitors created by code.
        rule_name: Filter by rule_name -> used
            in monitors created by code.
        search: Filter by: description, field,
            table, rule name, creator, namespace.
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
    op_selection = op.get_all_user_defined_monitors_v2(
        **strip_kwargs(
            user_defined_monitor_types=user_defined_monitor_types,
            created_by=created_by,
            order_by=order_by,
            entities=entities,
            description_field_or_table=description_field_or_table,
            domain_id=domain_id,
            is_template_managed=is_template_managed,
            namespace=namespace,
            rule_name=rule_name,
            search=search,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).edges(**strip_kwargs())

    op_stack = (
        "getAllUserDefinedMonitorsV2",
        "edges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getAllUserDefinedMonitorsV2"]["edges"]


@task
async def query_get_all_user_defined_monitors_v2_page_info(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    user_defined_monitor_types: Iterable[str] = None,
    created_by: Iterable[str] = None,
    order_by: str = None,
    entities: Iterable[str] = None,
    description_field_or_table: Iterable[str] = None,
    domain_id: datetime = None,
    is_template_managed: bool = None,
    namespace: Iterable[str] = None,
    rule_name: Iterable[str] = None,
    search: Iterable[str] = None,
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
        user_defined_monitor_types: Filter by
            monitor type.
        created_by: Filter by creator.
        order_by: Sorting of results.
        entities: Filter by associated entities
            (tables).
        description_field_or_table: Match text
            on rule description, table, or field.
        domain_id: Filter by domain UUID.
        is_template_managed: Filter monitors
            created by code.
        namespace: Filter by namespace -> used
            in monitors created by code.
        rule_name: Filter by rule_name -> used
            in monitors created by code.
        search: Filter by: description, field,
            table, rule name, creator, namespace.
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
    op_selection = op.get_all_user_defined_monitors_v2(
        **strip_kwargs(
            user_defined_monitor_types=user_defined_monitor_types,
            created_by=created_by,
            order_by=order_by,
            entities=entities,
            description_field_or_table=description_field_or_table,
            domain_id=domain_id,
            is_template_managed=is_template_managed,
            namespace=namespace,
            rule_name=rule_name,
            search=search,
            before=before,
            after=after,
            first=first,
            last=last,
        )
    ).page_info(**strip_kwargs())

    op_stack = (
        "getAllUserDefinedMonitorsV2",
        "pageInfo",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getAllUserDefinedMonitorsV2"]["pageInfo"]
