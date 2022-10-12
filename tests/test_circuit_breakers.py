import pytest
from prefect import flow
from pycarlo.common.errors import GqlError
from pycarlo.features.circuit_breakers.exceptions import CircuitBreakerPollException

from prefect_monte_carlo.circuit_breakers import (
    circuit_breaker_is_flipped,
    skip_if_circuit_breaker_flipped,
)


async def test_circuit_breaker_by_uuid_no_rule_breach(
    mock_monte_carlo_creds, mock_no_breach_of_rule, random_uuid
):
    @flow(name="test")
    @skip_if_circuit_breaker_flipped(
        rule_uuid=random_uuid, monte_carlo_credentials=mock_monte_carlo_creds
    )
    def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = test_flow(return_state=True)
    assert test_flow.name == "test"
    assert state.name == "Completed"
    assert test_flow.has_been_called


async def test_circuit_breaker_by_uuid_with_rule_breach(
    mock_monte_carlo_creds, mock_breach_of_rule, random_uuid
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_uuid=random_uuid, monte_carlo_credentials=mock_monte_carlo_creds
    )
    def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = test_flow(return_state=True)
    assert state.name == "Cancelled"
    assert not test_flow.has_been_called


async def test_circuit_breaker_by_name_with_rule_breach(
    mock_monte_carlo_creds,
    mock_breach_of_rule,
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_name="test_rule", monte_carlo_credentials=mock_monte_carlo_creds
    )
    def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = test_flow(return_state=True)
    assert state.name == "Cancelled"
    assert not test_flow.has_been_called


async def test_circuit_breaker_by_name_with_no_rule_breach(
    mock_monte_carlo_creds,
    mock_no_breach_of_rule,
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_name="test_rule", monte_carlo_credentials=mock_monte_carlo_creds
    )
    def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = test_flow(return_state=True)
    assert state.name == "Completed"
    assert test_flow.has_been_called


async def test_circuit_breaker_on_async_flow_by_uuid_no_rule_breach(
    mock_monte_carlo_creds, mock_no_breach_of_rule, random_uuid
):
    @flow(name="test")
    @skip_if_circuit_breaker_flipped(
        rule_uuid=random_uuid, monte_carlo_credentials=mock_monte_carlo_creds
    )
    async def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = await test_flow(return_state=True)
    assert test_flow.name == "test"
    assert state.name == "Completed"
    assert test_flow.has_been_called


async def test_circuit_breaker_on_async_flow_by_uuid_with_rule_breach(
    mock_monte_carlo_creds, mock_breach_of_rule, random_uuid
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_uuid=random_uuid, monte_carlo_credentials=mock_monte_carlo_creds
    )
    async def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = await test_flow(return_state=True)
    assert state.name == "Cancelled"
    assert not test_flow.has_been_called


async def test_circuit_breaker_on_async_flow_by_name_with_rule_breach(
    mock_monte_carlo_creds,
    mock_breach_of_rule,
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_name="test_rule", monte_carlo_credentials=mock_monte_carlo_creds
    )
    async def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = await test_flow(return_state=True)
    assert state.name == "Cancelled"
    assert not test_flow.has_been_called


async def test_circuit_breaker_on_async_flow_by_name_with_no_rule_breach(
    mock_monte_carlo_creds,
    mock_no_breach_of_rule,
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_name="test_rule", monte_carlo_credentials=mock_monte_carlo_creds
    )
    async def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = await test_flow(return_state=True)
    assert state.name == "Completed"
    assert test_flow.has_been_called


async def test_invalid_rule_reference_none_passed(
    mock_monte_carlo_creds,
):
    @flow
    @skip_if_circuit_breaker_flipped(monte_carlo_credentials=mock_monte_carlo_creds)
    def test_flow():
        pass

    with pytest.raises(ValueError):
        test_flow()


async def test_invalid_rule_reference_both_passed(
    mock_monte_carlo_creds,
    random_uuid,
):
    @flow
    @skip_if_circuit_breaker_flipped(
        monte_carlo_credentials=mock_monte_carlo_creds,
        rule_uuid=random_uuid,
        rule_name="test_rule",
    )
    def test_flow():
        pass

    with pytest.raises(ValueError):
        test_flow()


async def test_invalid_rule_reference_bad_uuid(
    mock_monte_carlo_creds,
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_uuid="bad_uuid", monte_carlo_credentials=mock_monte_carlo_creds
    )
    def test_flow():
        pass

    with pytest.raises(ValueError):
        test_flow()


async def test_ambiguous_rule_name_passed(
    monte_carlo_creds, mock_bad_operation_response
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_name="duplicate_name", monte_carlo_credentials=monte_carlo_creds
    )
    def test_flow():
        pass

    with pytest.raises(GqlError):
        test_flow()


async def test_circuit_breaker_is_not_flipped(
    mock_monte_carlo_creds, random_uuid, mock_circuit_breaker_is_not_flipped
):
    @flow
    def test_flow():
        return circuit_breaker_is_flipped(
            monte_carlo_credentials=mock_monte_carlo_creds, rule_uuid=random_uuid
        )

    breaker_is_flipped = test_flow()

    assert not breaker_is_flipped


async def test_circuit_breaker_is_flipped(
    mock_monte_carlo_creds, random_uuid, mock_circuit_breaker_is_flipped
):
    @flow
    def test_flow():
        return circuit_breaker_is_flipped(
            monte_carlo_credentials=mock_monte_carlo_creds, rule_uuid=random_uuid
        )

    breaker_is_flipped = test_flow()

    assert breaker_is_flipped


async def test_circuit_breaker_poll_error_raised(
    mock_monte_carlo_creds, random_uuid, mock_failed_polling
):
    @flow
    def test_flow():
        circuit_breaker_is_flipped(
            monte_carlo_credentials=mock_monte_carlo_creds, rule_uuid=random_uuid
        )

    with pytest.raises(CircuitBreakerPollException):
        test_flow()
