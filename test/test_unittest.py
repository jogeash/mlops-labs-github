import unittest
from src.throttle_checker import APIRequestThrottle, simulate_api_requests


class TestAPIRequestThrottle(unittest.TestCase):

    def test_remaining_requests(self):
        throttle = APIRequestThrottle(5, 60)
        throttle.register_request()
        self.assertEqual(throttle.remaining_requests(), 4)

    def test_exceed_limit(self):
        throttle = APIRequestThrottle(1, 60)
        throttle.register_request()
        with self.assertRaises(Exception):
            throttle.register_request()

    def test_simulated_requests(self):
        processed = simulate_api_requests()
        self.assertTrue(processed > 0)
        self.assertTrue(processed <= 40)


if __name__ == "__main__":
    unittest.main()
