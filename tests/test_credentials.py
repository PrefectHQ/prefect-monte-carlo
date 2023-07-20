from pycarlo.core import Client


async def test_monte_carlo_credentials_get_client(monte_carlo_creds):
    mc_client = monte_carlo_creds.get_client()

    assert isinstance(mc_client, Client)
