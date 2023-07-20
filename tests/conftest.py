from asyncio import Future
from unittest.mock import MagicMock
from uuid import uuid4

import pytest
from box import BoxList
from pycarlo.common.errors import GqlError
from pycarlo.features.circuit_breakers.exceptions import CircuitBreakerPollException

from prefect_monte_carlo.credentials import MonteCarloCredentials
from prefect_monte_carlo.lineage import MonteCarloLineageNode


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
                "name": "ecommerce_system",
                "type": None,
                "id": "UmVzb3VyY2U6M2NjNDFiYTEtMTMyYy00M2NkLWI2ZWEtZWE2OGZlNGEyOTA2",
                "uuid": "3cc41ba1-132c-43cd-b6ea-ea68fe4a2906",
                "is_default": False,
                "is_user_provided": True,
            },
        ]
    )


@pytest.fixture
def mock_circuit_breaker_is_not_flipped(monkeypatch):
    circuit_breaker_service = MagicMock()

    circuit_breaker_service.trigger.return_value = random_uuid
    circuit_breaker_service.poll.return_value = 0

    monkeypatch.setattr(
        "prefect_monte_carlo.circuit_breakers.CircuitBreakerService",
        MagicMock(return_value=circuit_breaker_service),
    )


@pytest.fixture
def mock_circuit_breaker_is_flipped(monkeypatch):
    circuit_breaker_service = MagicMock()

    circuit_breaker_service.trigger.return_value = random_uuid
    circuit_breaker_service.poll.return_value = 100

    monkeypatch.setattr(
        "prefect_monte_carlo.circuit_breakers.CircuitBreakerService",
        MagicMock(return_value=circuit_breaker_service),
    )


@pytest.fixture
def mock_monte_carlo_resources_response(monkeypatch, mock_monte_carlo_resources):
    monkeypatch.setattr(
        "pycarlo.core.Client.__call__",
        MagicMock(return_value=mock_monte_carlo_resources),
    )


@pytest.fixture
def mock_failed_polling(monkeypatch):
    monkeypatch.setattr(
        "prefect_monte_carlo.circuit_breakers.CircuitBreakerService.poll",
        MagicMock(side_effect=CircuitBreakerPollException),
    )


@pytest.fixture
def mock_source_model():
    return MonteCarloLineageNode(
        node_name="source_dataset",
        object_id="source_dataset",
        object_type="table",
        resource_name="ecommerce_system",
        tags=[{"propertyName": "dataset_owner", "propertyValue": "some_team"}],
    )


@pytest.fixture
def mock_destination_model():
    return MonteCarloLineageNode(
        node_name="destination_dataset",
        object_id="destination_dataset",
        object_type="table",
        resource_name="bigquery-2021-12-01",
        tags=[{"propertyName": "dataset_owner", "propertyValue": "some_team"}],
    )


@pytest.fixture
def mock_mcon():
    return "MCON++someid++table++source_raw_customer"


@pytest.fixture
def mock_edge_id():
    return "e3546a7dc6ee45f0eb63fda79dbc5de4994ffe2471c136aa057b95d3f9e5bd2e"

@pytest.fixture
def mock_job_ts():
    return 1639478400


@pytest.fixture
def mock_create_or_update_node_response(mock_mcon):
    return {"create_or_update_lineage_node": {"node": {"mcon": mock_mcon}}}


@pytest.fixture
def mock_create_or_update_edge_response(mock_job_ts):
    return {"create_or_update_lineage_edge": {"edge": {"jobTs": mock_job_ts}}}


@pytest.fixture
def mock_create_or_update_lineage_node(monkeypatch, mock_mcon):

    future = Future()
    future.set_result(mock_mcon)

    monkeypatch.setattr(
        "prefect_monte_carlo.lineage.create_or_update_lineage_node",
        MagicMock(return_value=future),
    )


@pytest.fixture
def mock_create_or_update_lineage_node_response(
    monkeypatch, mock_create_or_update_node_response
):

    monkeypatch.setattr(
        "pycarlo.core.Client.__call__",
        MagicMock(return_value=mock_create_or_update_node_response),
    )


@pytest.fixture
def mock_create_or_update_lineage_edge_response(
    monkeypatch, mock_create_or_update_edge_response
):

    monkeypatch.setattr(
        "pycarlo.core.Client.__call__",
        MagicMock(return_value=mock_create_or_update_edge_response),
    )


@pytest.fixture
def mock_create_or_update_lineage_edge(monkeypatch, mock_edge_id):

    future = Future()
    future.set_result(mock_edge_id)

    monkeypatch.setattr(
        "prefect_monte_carlo.lineage.create_or_update_lineage_edge",
        MagicMock(return_value=future),
    )
