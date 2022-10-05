import pytest
from prefect import flow
from pycarlo.common.errors import GqlError

from prefect_monte_carlo.circuit_breakers import skip_if_circuit_breaker_flipped


async def test_circuit_breaker_by_uuid_no_rule_breach(
    monte_carlo_credentials, mock_no_breach_of_rule, random_uuid
):
    @flow(name="test")
    @skip_if_circuit_breaker_flipped(
        rule_uuid=random_uuid, monte_carlo_credentials=monte_carlo_credentials
    )
    def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = test_flow(return_state=True)
    assert test_flow.name == "test"
    assert state.name == "Completed"
    assert test_flow.has_been_called


async def test_circuit_breaker_by_uuid_with_rule_breach(
    monte_carlo_credentials, mock_breach_of_rule, random_uuid
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_uuid=random_uuid, monte_carlo_credentials=monte_carlo_credentials
    )
    def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = test_flow(return_state=True)
    assert state.name == "Cancelled"
    assert not test_flow.has_been_called


async def test_circuit_breaker_by_name_with_rule_breach(
    monte_carlo_credentials,
    mock_breach_of_rule,
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_name="test_rule", monte_carlo_credentials=monte_carlo_credentials
    )
    def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = test_flow(return_state=True)
    assert state.name == "Cancelled"
    assert not test_flow.has_been_called


async def test_circuit_breaker_by_name_with_no_rule_breach(
    monte_carlo_credentials,
    mock_no_breach_of_rule,
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_name="test_rule", monte_carlo_credentials=monte_carlo_credentials
    )
    def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = test_flow(return_state=True)
    assert state.name == "Completed"
    assert test_flow.has_been_called


async def test_circuit_breaker_on_async_flow_by_uuid_no_rule_breach(
    monte_carlo_credentials, mock_no_breach_of_rule, random_uuid
):
    @flow(name="test")
    @skip_if_circuit_breaker_flipped(
        rule_uuid=random_uuid, monte_carlo_credentials=monte_carlo_credentials
    )
    async def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = await test_flow(return_state=True)
    assert test_flow.name == "test"
    assert state.name == "Completed"
    assert test_flow.has_been_called


async def test_circuit_breaker_on_async_flow_by_uuid_with_rule_breach(
    monte_carlo_credentials, mock_breach_of_rule, random_uuid
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_uuid=random_uuid, monte_carlo_credentials=monte_carlo_credentials
    )
    async def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = await test_flow(return_state=True)
    assert state.name == "Cancelled"
    assert not test_flow.has_been_called


async def test_circuit_breaker_on_async_flow_by_name_with_rule_breach(
    monte_carlo_credentials,
    mock_breach_of_rule,
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_name="test_rule", monte_carlo_credentials=monte_carlo_credentials
    )
    async def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = await test_flow(return_state=True)
    assert state.name == "Cancelled"
    assert not test_flow.has_been_called


async def test_circuit_breaker_on_async_flow_by_name_with_no_rule_breach(
    monte_carlo_credentials,
    mock_no_breach_of_rule,
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_name="test_rule", monte_carlo_credentials=monte_carlo_credentials
    )
    async def test_flow():
        test_flow.has_been_called = True

    test_flow.has_been_called = False

    state = await test_flow(return_state=True)
    assert state.name == "Completed"
    assert test_flow.has_been_called


async def test_circuit_breaker_ambiguous_rule_name(
    monte_carlo_credentials,
    mock_ambiguous_rule_name,
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_name="test_rule", monte_carlo_credentials=monte_carlo_credentials
    )
    def test_flow():
        pass

    with pytest.raises(GqlError):
        test_flow()


async def test_invalid_rule_reference_none_passed(
    monte_carlo_credentials,
):
    @flow
    @skip_if_circuit_breaker_flipped(monte_carlo_credentials=monte_carlo_credentials)
    def test_flow():
        pass

    with pytest.raises(ValueError):
        test_flow()


async def test_invalid_rule_reference_bad_uuid(
    monte_carlo_credentials,
):
    @flow
    @skip_if_circuit_breaker_flipped(
        rule_uuid="bad_uuid", monte_carlo_credentials=monte_carlo_credentials
    )
    def test_flow():
        pass

    with pytest.raises(ValueError):
        test_flow()
