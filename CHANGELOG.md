# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

- The `skip_if_circuit_breaker_flipped` decorator, underlying task `circuit_breaker_is_flipped`, and their tests. - [#5](https://github.com/PrefectHQ/prefect-monte-carlo/pull/5)
- The `rule_uuid_from_name` as a convenience method to retrieve rule uuids when names are passed. - [#5](https://github.com/PrefectHQ/prefect-monte-carlo/pull/5)
- The `resources` submodule for the `get_monte_carlo_resources` task to retrieve a list of all Monte Carlo Graphql resources via the pycarlo client - [#7](https://github.com/PrefectHQ/prefect-monte-carlo/issues/7).

### Changed

### Deprecated

### Removed

### Fixed

### Security
