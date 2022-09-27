"""
This is a module containing:
Montecarlo query_get_dbt_test_results* tasks
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
    Path(__file__).parent.resolve() / "configs" / "query" / "get_dbt_test_results.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_get_dbt_test_results(  # noqa
    run_start_time: datetime,
    run_end_time: datetime,
    montecarlo_credentials: MontecarloCredentials,
    first: int = None,
    after: str = None,
    last: int = None,
    before: str = None,
    status: Iterable[str] = None,
    model: Iterable[str] = None,
    mcon: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        run_start_time: Beginning of time window to match run start times.
        run_end_time: End of time window to match run start times.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        first: When paging forward: the number of items to return (page size).
        after: When paging forward: the cursor of the last item on the previous
            page of results.
        last: When paging backward: the number of items to return (page size).
        before: When paging backward: the cursor of the first item on the next
            page of results.
        status: Status(es) to match run results.
        model: dbt model ids to filter run results.
        mcon: Associated table MCONs to filter run results.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_dbt_test_results(
        **strip_kwargs(
            run_start_time=run_start_time,
            run_end_time=run_end_time,
            first=first,
            after=after,
            last=last,
            before=before,
            status=status,
            model=model,
            mcon=mcon,
        )
    )

    op_stack = ("getDbtTestResults",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDbtTestResults"]


@task
async def query_get_dbt_test_results_edges(  # noqa
    run_start_time: datetime,
    run_end_time: datetime,
    montecarlo_credentials: MontecarloCredentials,
    first: int = None,
    after: str = None,
    last: int = None,
    before: str = None,
    status: Iterable[str] = None,
    model: Iterable[str] = None,
    mcon: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Contains the nodes in this connection.

    Args:
        run_start_time: Beginning of time window to match
            run start times.
        run_end_time: End of time window to match run start
            times.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        first: When paging forward: the number of items to
            return (page size).
        after: When paging forward: the cursor of the last
            item on the previous page of results.
        last: When paging backward: the number of items to
            return (page size).
        before: When paging backward: the cursor of the
            first item on the next page of results.
        status: Status(es) to match run results.
        model: dbt model ids to filter run results.
        mcon: Associated table MCONs to filter run results.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_dbt_test_results(
        **strip_kwargs(
            run_start_time=run_start_time,
            run_end_time=run_end_time,
            first=first,
            after=after,
            last=last,
            before=before,
            status=status,
            model=model,
            mcon=mcon,
        )
    ).edges(**strip_kwargs())

    op_stack = (
        "getDbtTestResults",
        "edges",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDbtTestResults"]["edges"]


@task
async def query_get_dbt_test_results_page_info(  # noqa
    run_start_time: datetime,
    run_end_time: datetime,
    montecarlo_credentials: MontecarloCredentials,
    first: int = None,
    after: str = None,
    last: int = None,
    before: str = None,
    status: Iterable[str] = None,
    model: Iterable[str] = None,
    mcon: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Pagination data for this connection.

    Args:
        run_start_time: Beginning of time window to match
            run start times.
        run_end_time: End of time window to match run start
            times.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        first: When paging forward: the number of items to
            return (page size).
        after: When paging forward: the cursor of the last
            item on the previous page of results.
        last: When paging backward: the number of items to
            return (page size).
        before: When paging backward: the cursor of the
            first item on the next page of results.
        status: Status(es) to match run results.
        model: dbt model ids to filter run results.
        mcon: Associated table MCONs to filter run results.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.get_dbt_test_results(
        **strip_kwargs(
            run_start_time=run_start_time,
            run_end_time=run_end_time,
            first=first,
            after=after,
            last=last,
            before=before,
            status=status,
            model=model,
            mcon=mcon,
        )
    ).page_info(**strip_kwargs())

    op_stack = (
        "getDbtTestResults",
        "pageInfo",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["getDbtTestResults"]["pageInfo"]
