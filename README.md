# prefect-montecarlo

## Welcome!

Prefect integrations for interacting with Montecarlo.

The tasks within this collection were created by a code generator using the service's GraphQL schema.

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

## Development

If you'd like to install a version of `prefect-montecarlo` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-montecarlo.git

cd prefect-montecarlo/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
