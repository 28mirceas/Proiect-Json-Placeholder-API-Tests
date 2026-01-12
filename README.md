# Restful Booker API Tests

## Description
API automation tests for Restful Booker using Python, Pytest and Requests.

## Project Structure
- api/ – API client methods
- tests/ – test cases
- conftest.py – pytest fixtures
- requirements.txt – dependencies

## Setup
```bash
pip install -r requirements.txt

## Run Tests
pytest -v
pytest tests/test_json_placeholder.py -v
pytest -k test_create_post -v

## Se Instaleaza pachetul pytest-html cu comanda:
pip install pytest pytest-html
## Se ruleaza cu comanda:
pytest --html=report.html --self-contained-html