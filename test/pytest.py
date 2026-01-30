import pytest
from src.throttle_checker import APIRequestThrottle, simulate_api_requests


def test_requests_within_limit():
    throttle = APIRequestThrottle(5, 60)
    for _ in range(5):
        throttle.register_request()
    assert throttle.remaining_requests() == 0


def test_limit_exceeded():
    throttle = APIRequestThrottle(2, 60)
    throttle.register_request()
    throttle.register_request()
    with pytest.raises(Exception):
        throttle.register_request()


def test_window_reset():
    throttle = APIRequestThrottle(3, 1)
    throttle.register_request()
    throttle.window_start_time -= 2
    throttle.register_request()
    assert throttle.request_count == 1


def test_sklearn_simulation():
    processed = simulate_api_requests()
    assert processed > 0
    assert processed <= 40
