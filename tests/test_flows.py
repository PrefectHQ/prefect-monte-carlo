from prefect_monte_carlo.flows import hello_and_goodbye


def test_hello_and_goodbye_flow():
    result = hello_and_goodbye()
    assert result == "Done"
