"""
Used for generating the repository from scratch.
"""
from pathlib import Path

from prefect_collection_generator.gql import populate_collection_repo

THIS_DIRECTORY = Path(__file__).parent.absolute()
REPO_DIRECTORY = THIS_DIRECTORY.parent

# # USE THIS IF NEED TO REGENERATE FROM SCRATCH; IF NOT SKIP TO NEXT SECTION
# from cookiecutter.main import cookiecutter

# extra_context = {
#     "full_name":  "Prefect Technologies",  # e.g. "Prefect Technologies, Inc.",
#     "email": "help@prefect.io",  # e.g. "help@prefect.io",
#     "github_organization": "PrefectHQ",  # e.g. "PrefectHQ",
#     "collection_name": "prefect-montecarlo",
#     "collection_short_description": "Prefect integrations interacting with prefect-montecarlo",  # noqa
# }

# collection_template_url = "https://github.com/PrefectHQ/prefect-collection-template"
# cookiecutter(
#     collection_template_url,
#     no_input=True,
#     checkout="generated_graphql",
#     extra_context=extra_context,
#     overwrite_if_exists=True
# )
# REPO_DIRECTORY = THIS_DIRECTORY / prefect-montecarlo  # redirects repo_directory

# UPDATE THESE AS DESIRED
service_name = "Montecarlo"  # e.g. GitHub
service_url = "https://api.getmontecarlo.com/graphql"  # e.g. https://api.github.com/graphql

headers = {
    "x-mcd-id": "",
    "x-mcd-token": "",
    "Content-Type": "application/json",
}

root_to_op_types = {
    # if None, generates all available op_types
    "query": None,  # e.g. ["repository", "pull_requests"]
    "mutation": None,  # e.g. ["add_star", "remove_star"]
}
overwrite = True
repo_directory = "../"

# NOTE! manually updated `Connection` to inherit from 
# `sgqlc.types.Type` instead of `sgqlc.types.relay.Connection`
populate_collection_repo(
    service_name,
    service_url,
    headers,
    root_to_op_types,
    repo_directory=REPO_DIRECTORY,
    overwrite=overwrite,
)
