"""Credential classes used to perform authenticated interactions with Montecarlo"""

from prefect.blocks.core import Block
from pycarlo.core import Client, Session
from pydantic import Field, SecretStr


class MontecarloCredentials(Block):
    """
    Block used to manage Montecarlo authentication.

    Attributes:
        token: the token to authenticate into Montecarlo.

    Examples:
        Load stored Montecarlo credentials:
        ```python
        from prefect_montecarlo import MontecarloCredentials
        montecarlo_credentials_block = MontecarloCredentials.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "Montecarlo Credentials"
    _logo_url = "https://images.g2crowd.com/uploads/product/image/large_detail/large_detail_77e7b92d230439f18a97440a32be055e/monte-carlo.png"  # noqa

    api_token: SecretStr = Field(
        default=...,
        description="The token to authenticate with Montecarlo's GraphQL API.",
    )

    api_token_id: SecretStr = Field(
        default=...,
        description="The ID associated with the Montecarlo API token.",
    )

    async def get_client(self) -> Client:
        """
        Gets an authenticated Montecarlo GraphQL client via pycarlo.

        Returns:
            An authenticated Montecarlo GraphQL client

        Example:
            Gets an authenticated Montecarlo GraphQL client.
            ```python
            from prefect import flow
            from prefect_montecarlo import execute_graphql_query
            from prefect_montecarlo.credentials import MontecarloCredentials

            @flow
            def example_execute_query():
                montecarlo_credentials = MontecarloCredentials.load(
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
                mcd_id=self.api_token_id.get_secret_value(),
                mcd_token=self.api_token.get_secret_value(),
            )
        )
