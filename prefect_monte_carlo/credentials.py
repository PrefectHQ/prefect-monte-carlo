"""Credential classes used to perform authenticated interactions with Monte Carlo"""

from typing import Optional

from prefect.blocks.core import Block
from pycarlo.core import Client, Session
from pydantic import VERSION as PYDANTIC_VERSION

if PYDANTIC_VERSION.startswith("2."):
    from pydantic.v1 import Field, SecretStr
else:
    from pydantic import Field, SecretStr


class MonteCarloCredentials(Block):
    """
    Block used to manage Monte Carlo authentication.

    Attributes:
        api_key: The Monte Carlo API key to authenticate with.
        api_key_id: The Monte Carlo API key ID to authenticate with.
        catalog_url: The URL of the Monte Carlo catalog to use.

    Example:
        Load stored Monte Carlo credentials:
        ```python
        from prefect_monte_carlo.credentials import MonteCarloCredentials
        montecarlo_credentials_block = MonteCarloCredentials.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "Monte Carlo Credentials"
    _logo_url = "https://cdn.sanity.io/images/3ugk85nk/production/624870fcf18298f6bf0efb55046e50765620eabd-72x72.png"  # noqa
    _documentation_url = "https://prefecthq.github.io/prefect-monte-carlo/credentials/#prefect_monte_carlo.credentials.MonteCarloCredentials"  # noqa

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

    catalog_url: Optional[str] = Field(
        default="https://getmontecarlo.com/catalog",
        title="Monte Carlo catalog URL",
        description="The URL of the Monte Carlo catalog.",
    )

    def get_client(self) -> Client:
        """
        Gets an authenticated Monte Carlo GraphQL client via pycarlo.

        Returns:
            An authenticated Monte Carlo GraphQL client.

        Example:
            Gets an authenticated Monte Carlo GraphQL client.
            ```python
            from prefect import flow
            from prefect_monte_carlo.graphql import execute_graphql_operation
            from prefect_monte_carlo.credentials import MonteCarloCredentials

            @flow
            def example_execute_query():
                monte_carlo_credentials = MonteCarloCredentials.load(
                    "my-montecarlo-credentials"
                )
                result = execute_graphql_operation(
                    monte_carlo_credentials=monte_carlo_credentials,
                    query="query getUser { getUser { email firstName lastName }}",
                )

            example_execute_query()
            ```
        """

        return Client(
            session=Session(
                mcd_id=self.api_key_id,
                mcd_token=self.api_key.get_secret_value(),
            )
        )
