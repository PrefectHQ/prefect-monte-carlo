"""This is an example flows module"""
from prefect import flow

from prefect_monte_carlo.blocks import MontecarloBlock
from prefect_monte_carlo.tasks import (
    goodbye_prefect_monte_carlo,
    hello_prefect_monte_carlo,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    MontecarloBlock.seed_value_for_example()
    block = MontecarloBlock.load("sample-block")

    print(hello_prefect_monte_carlo())
    print(f"The block's value: {block.value}")
    print(goodbye_prefect_monte_carlo())
    return "Done"


if __name__ == "__main__":
    hello_and_goodbye()
