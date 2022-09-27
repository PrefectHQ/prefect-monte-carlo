"""
This is a module containing:
Montecarlo query_get_field_bi_lineage* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_field_bi_lineage.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_field_bi_lineage(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    full_table_id: str = None,
    field_name: str = None,
    last_seen_range_start: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        full_table_id: None.
        field_name: None.
        last_seen_range_start: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_field_bi_lineage(
        **strip_kwargs(
            full_table_id=full_table_id,
            field_name=field_name,
            last_seen_range_start=last_seen_range_start,
        )
    )

    op_stack = ("getFieldBiLineage",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getFieldBiLineage"]
