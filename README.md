# API Request Throttle Checker

This project simulates API rate-limiting logic using a fixed request limit
within a time window. A scikit-learn dataset (Wine) is used to simulate
incoming API requests.

## Features
- Rate limit validation
- Time window reset
- Remaining request calculation
- Pytest and Unittest coverage
- GitHub Actions CI

## Run Locally
```bash
pip install -r requirements.txt
pytest
python -m unittest discover
