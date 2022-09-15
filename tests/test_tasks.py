from prefect import flow

from prefect_monte_carlo.tasks import (
    goodbye_prefect_monte_carlo,
    hello_prefect_monte_carlo,
)


def test_hello_prefect_monte_carlo():
    @flow
    def test_flow():
        return hello_prefect_monte_carlo()

    result = test_flow()
    assert result == "Hello, prefect-monte-carlo!"


def goodbye_hello_prefect_monte_carlo():
    @flow
    def test_flow():
        return goodbye_prefect_monte_carlo()

    result = test_flow()
    assert result == "Goodbye, prefect-monte-carlo!"
