import pytest
from api.json_placeholder import get_posts,get_post,create_post,update_post,partial_update_post,delete_post


def test_get_posts(base_url):
    response = get_posts(base_url)
    assert response.status_code == 200, "Unexpected status code"


def test_create_post(base_url,default_request_body):
    response = create_post(base_url, default_request_body)
    assert response.status_code == 201, "Unexpected status code"
    assert response.json()["title"] == default_request_body["title"]


def test_get_post(base_url):
    response = get_post(base_url, post_id=1)
    assert response.status_code == 200


@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_post_data_driven(base_url, post_id):
    response = get_post(base_url, post_id)
    assert response.status_code == 200
    assert response.json()["id"] == post_id


def test_update_post(base_url, default_request_body):
    updated_body = default_request_body
    updated_body["id"] = 1

    response = update_post(base_url, updated_body, post_id=1)
    assert response.status_code == 200
    assert response.json()["title"] == default_request_body["title"]


def test_partial_update_post(base_url):
    response = partial_update_post(base_url, {"title": "foo3" }, post_id=1)

    assert response.status_code == 200
    assert response.json()["title"] == "foo3"


def test_delete_post(base_url):
    response = delete_post(base_url, post_id=1)
    assert response.status_code == 200
