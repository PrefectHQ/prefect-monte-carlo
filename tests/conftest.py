import pytest

from prefect_montecarlo.credentials import MontecarloCredentials
from pycarlo.common.errors import GqlError
from unittest.mock import MagicMock

@pytest.fixture
def montecarlo_credentials():
    return MontecarloCredentials(
        api_token="test-token",
        api_token_id="test-token-id",
    )

@pytest.fixture
def sample_get_tables_query_response():
    return {
        "get_tables":{
            "edges":[
                {
                    "node":{
                    "full_table_id":"dev:jaffle_shop.stg_customers"
                    }
                },
                {
                    "node":{
                    "full_table_id":"dev:jaffle_shop.stg_payments"
                    }
                },
                {
                    "node":{
                    "full_table_id":"dev:jaffle_shop.stg_orders"
                    }
                },
                {
                    "node":{
                    "full_table_id":"dev:jaffle_shop.raw_orders"
                    }
                },
                {
                    "node":{
                    "full_table_id":"dev:jaffle_shop.raw_customers"
                    }
                },
                {
                    "node":{
                    "full_table_id":"dev:jaffle_shop.orders"
                    }
                },
                {
                    "node":{
                    "full_table_id":"dev:jaffle_shop.customers"
                    }
                },
                {
                    "node":{
                    "full_table_id":"dev:jaffle_shop.raw_payments"
                    }
                },
            ]
        }
    }

@pytest.fixture
def mock_successful_get_tables_query_response(
    monkeypatch,
    sample_get_tables_query_response
):
    monkeypatch.setattr(
        "pycarlo.core.Client.__call__",
        MagicMock(return_value=sample_get_tables_query_response)
    )

@pytest.fixture
def mock_bad_variable_get_tables_query_response(
    monkeypatch
):
    monkeypatch.setattr(
        "pycarlo.core.Client.__call__",
        MagicMock(side_effect=GqlError)
    )