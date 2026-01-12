import pytest

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def default_request_body():
    return {
        "title": "titlu_nou2",
        "body": "Corp titlu nou2!",
        "userId": 1
    }
