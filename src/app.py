import time
from sklearn.datasets import load_wine


class APIRequestThrottle:
    """
    Simulates API rate-limiting logic within a fixed time window.
    """

    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.request_count = 0
        self.window_start_time = time.time()

    def register_request(self):
        self._reset_if_window_expired()
        if self.request_count >= self.max_requests:
            raise Exception("API rate limit exceeded")
        self.request_count += 1

    def remaining_requests(self):
        self._reset_if_window_expired()
        return self.max_requests - self.request_count

    def is_limit_exceeded(self):
        self._reset_if_window_expired()
        return self.request_count >= self.max_requests

    def _reset_if_window_expired(self):
        if time.time() - self.window_start_time >= self.window_seconds:
            self.request_count = 0
            self.window_start_time = time.time()


def simulate_api_requests():
    """
    Uses sklearn Wine dataset to simulate API requests.
    Each record = one API request.
    """
    data = load_wine()
    throttle = APIRequestThrottle(max_requests=40, window_seconds=60)

    processed = 0
    for _ in data.data:
        try:
            throttle.register_request()
            processed += 1
        except Exception:
            break

    return processed
