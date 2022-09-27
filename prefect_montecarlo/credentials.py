"""Credential classes used to perform authenticated interactions with Montecarlo"""

from prefect.blocks.core import Block
from pydantic import Field, SecretStr
from sgqlc.endpoint.requests import RequestsEndpoint


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
    
    def get_endpoint(self) -> RequestsEndpoint:
        """
        Gets an authenticated Montecarlo GraphQL RequestsEndpoint.

        Returns:
            An authenticated Montecarlo GraphQL RequestsEndpoint

        Example:
            Gets an authenticated Montecarlo GraphQL RequestsEndpoint.
            ```python
            from prefect import flow
            from prefect_montecarlo import run_custom_query
            from prefect_montecarlo.credentials import MontecarloCredentials

            @flow
            def example_run_custom_query():
                montecarlo_credentials = MontecarloCredentials.load(
                    "my-montecarlo-credentials"
                )
                result = run_custom_query(
                    montecarlo_credentials=montecarlo_credentials,
                    query="query getTables{ getTables(first:3) { edges { node { fullTableId } } } }",
                )

            example_get_endpoint_flow()
            ```
        """
        base_headers = {
            "x-mcd-id": self.api_token_id.get_secret_value(),
            "x-mcd-token": self.api_token.get_secret_value(),
            "Content-Type": "application/json",
        }

        endpoint = RequestsEndpoint(
            "https://api.getmontecarlo.com/graphql", base_headers=base_headers
        )
        return endpoint
