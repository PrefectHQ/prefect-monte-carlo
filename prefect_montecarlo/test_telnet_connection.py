"""
This is a module containing:
Montecarlo query_test_telnet_connection* tasks
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
    / "test_telnet_connection.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_test_telnet_connection(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    host: str = None,
    port: int = None,
    timeout: int = None,
    dc_id: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """


    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        host: Host to check.
        port: Port to check.
        timeout: Timeout in seconds.
        dc_id: DC UUID. To disambiguate accounts with multiple collectors.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.test_telnet_connection(
        **strip_kwargs(
            host=host,
            port=port,
            timeout=timeout,
            dc_id=dc_id,
        )
    )

    op_stack = ("testTelnetConnection",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testTelnetConnection"]


@task
async def query_test_telnet_connection_warnings(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    host: str = None,
    port: int = None,
    timeout: int = None,
    dc_id: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of warnings of failed validations.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        host: Host to check.
        port: Port to check.
        timeout: Timeout in seconds.
        dc_id: DC UUID. To disambiguate accounts with
            multiple collectors.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.test_telnet_connection(
        **strip_kwargs(
            host=host,
            port=port,
            timeout=timeout,
            dc_id=dc_id,
        )
    ).warnings(**strip_kwargs())

    op_stack = (
        "testTelnetConnection",
        "warnings",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testTelnetConnection"]["warnings"]


@task
async def query_test_telnet_connection_validations(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    host: str = None,
    port: int = None,
    timeout: int = None,
    dc_id: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List of validations that passed.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        host: Host to check.
        port: Port to check.
        timeout: Timeout in seconds.
        dc_id: DC UUID. To disambiguate accounts with
            multiple collectors.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.test_telnet_connection(
        **strip_kwargs(
            host=host,
            port=port,
            timeout=timeout,
            dc_id=dc_id,
        )
    ).validations(**strip_kwargs())

    op_stack = (
        "testTelnetConnection",
        "validations",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testTelnetConnection"]["validations"]
