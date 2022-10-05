from unittest.mock import MagicMock
from uuid import uuid4

import pytest
from pycarlo.common.errors import GqlError
from pycarlo.core import Client

from prefect_monte_carlo.credentials import MonteCarloCredentials


@pytest.fixture
def monte_carlo_credentials():
    return MonteCarloCredentials(
        api_key="test-token",
        api_key_id="test-token-id",
    )


@pytest.fixture
def random_uuid():
    return str(uuid4())


@pytest.fixture
def sample_get_tables_query_response():
    return {
        "get_tables": {
            "edges": [
                {"node": {"full_table_id": "dev:jaffle_shop.stg_customers"}},
                {"node": {"full_table_id": "dev:jaffle_shop.stg_payments"}},
                {"node": {"full_table_id": "dev:jaffle_shop.stg_orders"}},
                {"node": {"full_table_id": "dev:jaffle_shop.raw_orders"}},
                {"node": {"full_table_id": "dev:jaffle_shop.raw_customers"}},
                {"node": {"full_table_id": "dev:jaffle_shop.orders"}},
                {"node": {"full_table_id": "dev:jaffle_shop.customers"}},
                {"node": {"full_table_id": "dev:jaffle_shop.raw_payments"}},
            ]
        }
    }


@pytest.fixture
def mock_successful_get_tables_query_response(
    monkeypatch, sample_get_tables_query_response
):
    monkeypatch.setattr(
        "pycarlo.core.Client.__call__",
        MagicMock(return_value=sample_get_tables_query_response),
    )


@pytest.fixture
def mock_bad_variable_get_tables_query_response(monkeypatch):
    monkeypatch.setattr("pycarlo.core.Client.__call__", MagicMock(side_effect=GqlError))


@pytest.fixture
def mock_no_breach_of_rule(monkeypatch):
    monkeypatch.setattr(
        "prefect_monte_carlo.circuit_breakers.is_monitor_rule_breached",
        MagicMock(return_value=False),
    )


@pytest.fixture
def mock_breach_of_rule(monkeypatch):
    monkeypatch.setattr(
        "prefect_monte_carlo.circuit_breakers.is_monitor_rule_breached",
        MagicMock(return_value=True),
    )


@pytest.fixture
def mock_ambiguous_rule_name(monkeypatch):
    monkeypatch.setattr(
        "prefect_monte_carlo.credentials.MonteCarloCredentials.get_client",
        MagicMock(return_value=Client()),
    )

    monkeypatch.setattr(
        "pycarlo.core.Client.__call__",
        MagicMock(side_effect=GqlError),
    )
