"""
This is a module containing:
Montecarlo query_get_lineage_node_properties* tasks
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
    / "get_lineage_node_properties.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_lineage_node_properties(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dw_id: datetime = None,
    node_ids: Iterable[str] = None,
    mcons: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dw_id: Warehouse the asset is contained within. Not required when using
            an mcon as node id.
        node_ids: Deprecated - use mcon. Ignored if mcon is present.
        mcons: List of mcons to get properties for.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_lineage_node_properties(
        **strip_kwargs(
            dw_id=dw_id,
            node_ids=node_ids,
            mcons=mcons,
        )
    )

    op_stack = ("getLineageNodeProperties",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getLineageNodeProperties"]
