from unittest.mock import MagicMock
from uuid import uuid4

import pytest
from box import BoxList
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
def mock_bad_operation_response(monkeypatch):
    monkeypatch.setattr(
        "pycarlo.core.Client.__call__",
        MagicMock(side_effect=GqlError),
    )


@pytest.fixture
def mock_monte_carlo_resources():
    return BoxList(
        [
            {
                "name": "Invalid date+01:00",
                "type": None,
                "id": "UmVzb3VyY2U6YzNlYTI5MjgtZjEyOC00NGViLWExNGUtZTU5YzY3M2RmYjI2",
                "uuid": "c3ea2928-f128-44eb-a14e-e59c673dfb26",
                "is_default": False,
                "is_user_provided": True,
            },
            {
                "name": "ecommerce_system",
                "type": None,
                "id": "UmVzb3VyY2U6M2NjNDFiYTEtMTMyYy00M2NkLWI2ZWEtZWE2OGZlNGEyOTA2",
                "uuid": "3cc41ba1-132c-43cd-b6ea-ea68fe4a2906",
                "is_default": False,
                "is_user_provided": True,
            },
            {
                "name": "bigquery-2021-12-09T11:47:30.306Z",
                "type": "bigquery",
                "id": "UmVzb3VyY2U6YjdlOWQ2OWItMDllYi00Y2ZlLTg0OTctN2E0ZTRiNTkyNTg4",
                "uuid": "b7e9d69b-09eb-4cfe-8497-7a4e4b592588",
                "is_default": False,
                "is_user_provided": False,
            },
            {
                "name": "data_lake",
                "type": None,
                "id": "UmVzb3VyY2U6M2E0M2JkNzQtZmY0YS00NmQ2LTkyM2UtNjM4Y2RjY2M0MjE4",
                "uuid": "3a43bd74-ff4a-46d6-923e-638cdccc4218",
                "is_default": False,
                "is_user_provided": True,
            },
            {
                "name": "GitHub",
                "type": None,
                "id": "UmVzb3VyY2U6MjkyZGM3YjgtODI3Ny00Y2NkLWJiZmUtNjI3Mjc2MjdjNDQ1",
                "uuid": "292dc7b8-8277-4ccd-bbfe-62727627c445",
                "is_default": False,
                "is_user_provided": True,
            },
            {
                "name": "shopify_new_resource",
                "type": None,
                "id": "UmVzb3VyY2U6YzkxYjVlYjQtZTQzYi00NGNjLWE1NDAtYzY3MTg0YjQ4M2Iy",
                "uuid": "c91b5eb4-e43b-44cc-a540-c67184b483b2",
                "is_default": False,
                "is_user_provided": True,
            },
            {
                "name": "crm",
                "type": "source_system",
                "id": "UmVzb3VyY2U6NDhhNDAzMjktNDRmMS00OWFmLWIzNDEtMmY4MjI1MmI2YmU2",
                "uuid": "48a40329-44f1-49af-b341-2f82252b6be6",
                "is_default": False,
                "is_user_provided": True,
            },
            {
                "name": "xxx",
                "type": "source_system",
                "id": "UmVzb3VyY2U6NjU3OTNhN2EtOGUxYy00NWY5LWE0NjMtYjdiZmUwZWNlNWMz",
                "uuid": "65793a7a-8e1c-45f9-a463-b7bfe0ece5c3",
                "is_default": False,
                "is_user_provided": True,
            },
            {
                "name": "default",
                "type": None,
                "id": "UmVzb3VyY2U6MmNjM2JjMzgtYjFmZS00ZTNkLTk2ODUtYmJjZjhiMzQ0N2Q1",
                "uuid": "2cc3bc38-b1fe-4e3d-9685-bbcf8b3447d5",
                "is_default": True,
                "is_user_provided": True,
            },
            {
                "name": "shopify",
                "type": "source_system",
                "id": "UmVzb3VyY2U6Yzg3NDRmYjItY2Q1Yi00OTFlLWI5N2MtMTJmYWNhNmYwOWJj",
                "uuid": "c8744fb2-cd5b-491e-b97c-12faca6f09bc",
                "is_default": False,
                "is_user_provided": True,
            },
            {
                "name": "data-lake",
                "type": "data-lake",
                "id": "UmVzb3VyY2U6ZWZjNzI3ZjktNGM0OC00N2I3LTk5MzQtZTJkM2IyY2IxNzQ3",
                "uuid": "efc727f9-4c48-47b7-9934-e2d3b2cb1747",
                "is_default": False,
                "is_user_provided": False,
            },
            {
                "name": "SNOWFLAKE_DEV",
                "type": "snowflake",
                "id": "UmVzb3VyY2U6ZWNhYWM3YjktYmRlMS00NTg1LTg1OTMtYWZiYjViZGJmMTJi",
                "uuid": "ecaac7b9-bde1-4585-8593-afbb5bdbf12b",
                "is_default": False,
                "is_user_provided": False,
            },
        ]  # noqa
    )


@pytest.fixture
def mock_monte_carlo_resources_response(monkeypatch, mock_monte_carlo_resources):
    monkeypatch.setattr(
        "pycarlo.core.Client.__call__",
        MagicMock(return_value=mock_monte_carlo_resources),
    )
