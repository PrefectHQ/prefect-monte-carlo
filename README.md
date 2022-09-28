# prefect-montecarlo

<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-montecarlo/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-montecarlo?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/PrefectHQ/prefect-montecarlo/" alt="Stars">
        <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-montecarlo?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-montecarlo/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-montecarlo?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/PrefectHQ/prefect-montecarlo/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-montecarlo?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-montecarlo-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect-montecarlo.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>

## Welcome!

A collection of Prefect tasks and flows to orchestrate Monte Carlo

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-montecarlo` with `pip`:

```bash
pip install prefect-montecarlo
```

### Write and run a flow

```python
from prefect import flow
from prefect_montecarlo.tasks import (
    goodbye_prefect_montecarlo,
    hello_prefect_montecarlo,
)


@flow
def example_flow():
    hello_prefect_montecarlo
    goodbye_prefect_montecarlo

example_flow()
```

## Resources

If you encounter any bugs while using `prefect-montecarlo`, feel free to open an issue in the [prefect-montecarlo](https://github.com/PrefectHQ/prefect-montecarlo) repository.

If you have any questions or issues while using `prefect-montecarlo`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to ⭐️ or watch [`prefect-montecarlo`](https://github.com/PrefectHQ/prefect-montecarlo) for updates too!

## Development

If you'd like to install a version of `prefect-montecarlo` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-montecarlo.git

cd prefect-montecarlo/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
