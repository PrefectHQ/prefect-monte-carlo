from prefect_montecarlo.credentials import MontecarloCredentials
from pycarlo.core import Client

async def test_montecarlo_credentials_get_client():
    mc_credentials = MontecarloCredentials(
        api_token="test-token",
        api_token_id="test-token-id",
    )
    
    mc_client = await mc_credentials.get_client()
    
    assert isinstance(mc_client, Client)