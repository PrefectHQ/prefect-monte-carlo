from unittest.mock import MagicMock
from uuid import uuid4

import pytest
from pycarlo.common.errors import GqlError

from prefect_monte_carlo.credentials import MonteCarloCredentials


@pytest.fixture
def mock_monte_carlo_creds():
    mock_client = MagicMock()
    mock_creds = MagicMock().get_client.return_value = mock_client

    return mock_creds


@pytest.fixture
def monte_carlo_creds():
    return MonteCarloCredentials(
        api_key="test_api_key",
        api_key_id="test_api_key_id",
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
def mock_no_breach_of_rule(monkeypatch):
    monkeypatch.setattr(
        "prefect_monte_carlo.circuit_breakers.circuit_breaker_is_flipped",
        MagicMock(return_value=False),
    )


@pytest.fixture
def mock_breach_of_rule(monkeypatch):
    monkeypatch.setattr(
        "prefect_monte_carlo.circuit_breakers.circuit_breaker_is_flipped",
        MagicMock(return_value=True),
    )


@pytest.fixture
def mock_bad_operation(monkeypatch):
    monkeypatch.setattr(
        "pycarlo.core.Client.__call__",
        MagicMock(side_effect=GqlError),
    )
