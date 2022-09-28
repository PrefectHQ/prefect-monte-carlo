from pycarlo.core import Client

async def test_montecarlo_credentials_get_client(montecarlo_credentials):
    
    mc_client = await montecarlo_credentials.get_client()
    
    assert isinstance(mc_client, Client)