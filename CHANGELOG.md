# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

## v0.1.0

Released October 14th, 2022.

### Added

- The `skip_if_circuit_breaker_flipped` decorator, underlying task `circuit_breaker_is_flipped`, and their tests. - [#5](https://github.com/PrefectHQ/prefect-monte-carlo/pull/5)
- The `rule_uuid_from_name` as a convenience method to retrieve rule uuids when names are passed. - [#5](https://github.com/PrefectHQ/prefect-monte-carlo/pull/5)
- The `resources` submodule for the `get_monte_carlo_resources` task to retrieve a list of all Monte Carlo Graphql resources via the pycarlo client - [#7](https://github.com/PrefectHQ/prefect-monte-carlo/issues/7).
- The `lineage` submodule containing `create_or_update_lineage`, `create_or_update_lineage_node`, `create_or_update_lineage_edge`, and a `MonteCarloLineageNode` pydantic model to allow users to fully specify valid lineage nodes. - [#13](https://github.com/PrefectHQ/prefect-monte-carlo/pull/13)
- The `utilities` submodule containing `rule_uuid_from_name` and `validate_tags`. - [#13](https://github.com/PrefectHQ/prefect-monte-carlo/pull/13)
