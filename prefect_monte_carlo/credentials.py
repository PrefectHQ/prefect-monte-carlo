"""Credential classes used to perform authenticated interactions with Monte Carlo"""

from prefect.blocks.core import Block
from pycarlo.core import Client, Session
from pydantic import Field, SecretStr


class MonteCarloCredentials(Block):
    """
    Block used to manage Monte Carlo authentication.

    Attributes:
        api_key: The Monte Carlo API key to authenticate with.
        api_key_id: The Monte Carlo API key ID to authenticate with.

    Examples:
        Load stored Monte Carlo credentials:
        ```python
        from prefect_monte_carlo import MonteCarloCredentials
        montecarlo_credentials_block = MonteCarloCredentials.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "Monte Carlo Credentials"
    _logo_url = "https://images.ctfassets.net/gm98wzqotmnx/5OqrPNRdLMvqZzxo9f6Z25/f920dff0f1201fc014b0b083a6d2fdb1/image.png?h=250"  # noqa

    api_key: SecretStr = Field(
        default=...,
        title="API Key",
        description="The token to authenticate with Monte Carlo's GraphQL API.",
    )

    api_key_id: str = Field(
        default=...,
        title="API Key ID",
        description="The ID associated with the Monte Carlo API token.",
    )

    def get_client(self) -> Client:
        """
        Gets an authenticated Monte Carlo GraphQL client via pycarlo.

        Returns:
            An authenticated Monte Carlo GraphQL client

        Example:
            Gets an authenticated Monte Carlo GraphQL client.
            ```python
            from prefect import flow
            from prefect_monte_carlo import execute_graphql_query
            from prefect_monte_carlo.credentials import MonteCarloCredentials

            @flow
            def example_execute_query():
                montecarlo_credentials = MonteCarloCredentials.load(
                    "my-montecarlo-credentials"
                )
                result = execute_graphql_query(
                    montecarlo_credentials=montecarlo_credentials,
                    query="query getUser { getUser { email firstName lastName }}",
                )

            example_execute_query()
            ```
        """

        return Client(
            session=Session(
                mcd_id=self.api_key.get_secret_value(),
                mcd_token=self.api_key_id,
            )
        )
