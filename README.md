# prefect-monte-carlo

Visit the full docs [here](https://PrefectHQ.github.io/prefect-monte-carlo) to see additional examples and the API reference.

<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-monte-carlo/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-monte-carlo?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/PrefectHQ/prefect-monte-carlo/" alt="Stars">
        <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-monte-carlo?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-monte-carlo/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-monte-carlo?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/PrefectHQ/prefect-monte-carlo/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-monte-carlo?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>

## Welcome!

A collection of Prefect tasks and flows to interact with Monte Carlo from workflows.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-monte-carlo` with `pip`:

```bash
pip install prefect-monte-carlo
```

Then, register this collection's blocks to [view them on Prefect Cloud](https://orion-docs.prefect.io/ui/blocks/):

```bash
prefect block register -m prefect_monte_carlo
```

Note, to use the `load` method on Blocks, you must already have a block document [saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).

### Write and run a flow
#### Execute a query against the Monte Carlo GraphQL API
```python
from prefect import flow
from prefect_monte_carlo.graphql import execute_graphql_operation
from prefect_monte_carlo.credentials import MonteCarloCredentials

@flow
def example_execute_query():
    monte_carlo_credentials = MonteCarloCredentials.load("my-mc-creds")
    result = execute_graphql_operation(
        monte_carlo_credentials=monte_carlo_credentials,
        operation="query getUser { getUser { email firstName lastName }}",
    )
```

#### Create or update Monte Carlo lineage
```python
from prefect import flow
from prefect.context import get_run_context
from prefect_monte_carlo.credentials import MonteCarloCredentials
from prefect_monte_carlo.lineage import create_or_update_lineage, MonteCarloLineageNode

@flow
def monte_carlo_orchestrator():
    current_flow_run_name = get_run_context().flow_run.name

    source = MonteCarloLineageNode(
        node_name="source_dataset",
        object_id="source_dataset",
        object_type="table",
        resource_name="some_resource_name",
        tags=[{"propertyName": "dataset_owner", "propertyValue": "owner_name"}],
    )

    destination = MonteCarloLineageNode(
        node_name="destination_dataset",
        object_id="destination_dataset",
        object_type="table",
        resource_name="some_resource_name",
        tags=[{"propertyName": "dataset_owner", "propertyValue": "owner_name"}],
    )

    # `create_or_update_lineage` is a flow, so this will be a subflow run
    # `extra_tags` are added to both the `source` and `destination` nodes
    create_or_update_lineage(
        monte_carlo_credentials=MonteCarloCredentials.load("my-mc-creds)
        source=source,
        destination=destination,
        expire_at=datetime.now() + timedelta(days=10),
        extra_tags=[{"propertyName": "flow_run_name", "propertyValue": current_flow_run_name}]
    )
```


#### Conditionally execute a flow based on a Monte Carlo circuit breaker rule
```python
from prefect import flow
from prefect_monte_carlo.circuit_breakers import skip_if_circuit_breaker_flipped
from prefect_monte_carlo.credentials import MonteCarloCredentials

my_mc_creds = MonteCarloCredentials.load("my-mc-creds")
rule_name = "myRule"

@flow
@skip_if_circuit_breaker_flipped(
    monte_carlo_credentials=my_mc_creds
    rule_name=rule_name,
)
def conditional_flow():
    logger = get_run_logger()
    logger.info("If you see this, your circuit breaker rule was not breached!")
```

## Resources

If you encounter any bugs while using `prefect-monte-carlo`, feel free to open an issue in the [prefect-monte-carlo](https://github.com/PrefectHQ/prefect-monte-carlo) repository.

If you have any questions or issues while using `prefect-monte-carlo`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to star or watch [`prefect-monte-carlo`](https://github.com/PrefectHQ/prefect-monte-carlo) for updates too!

## Contributing

If you'd like to help contribute to fix an issue or add a feature to `prefect-monte-carlo`, please [propose changes through a pull request from a fork of the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

Here are the steps:

1. [Fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository)
2. [Clone the forked repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository)
3. Install the repository and its dependencies:
```
pip install -e ".[dev]"
```
4. Make desired changes
5. Add tests
6. Insert an entry to [CHANGELOG.md](https://github.com/PrefectHQ/prefect-monte-carlo/blob/main/CHANGELOG.md)
7. Install `pre-commit` to perform quality checks prior to commit:

```
pre-commit install
```
8. `git commit`, `git push`, and create a pull request
