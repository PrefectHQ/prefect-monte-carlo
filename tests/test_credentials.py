import pytest
from sgqlc.endpoint.http import HTTPEndpoint

from prefect_montecarlo import MontecarloCredentials


@pytest.mark.parametrize("token", [None, "token_value"])
def test_montecarlo_credentials_get_endpoint(token):
    endpoint = MontecarloCredentials(token=token).get_endpoint()
    assert isinstance(endpoint, HTTPEndpoint)
    if token is not None:
        assert endpoint.base_headers == {"Authorization": "Bearer token_value"}
