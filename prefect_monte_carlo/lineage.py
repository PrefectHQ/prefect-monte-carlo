from typing import Dict

from prefect import task


@task
def create_or_update_lineage() -> Dict:
    pass


@task
def create_or_update_node_with_tags() -> str:
    pass
