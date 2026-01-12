from api.json_placeholder import (get_posts,get_post,create_post,update_post,
                                  partial_update_post,delete_post)


def test_get_post_with_non_exist_post_id(base_url):
    """
    BUG:
    API returns 200 OK with empty body for non-existent post ID.
    Expected behavior: 404 Not Found.
    """
    response = get_post(base_url, post_id=9999)
    assert response.status_code == 200
    assert response.json() == {}, "Expected empty response body for non-existent post ID"


def test_create_post_with_wrong_body(base_url,default_request_body):
    """
    API does not validate request body.
    Expected behavior: 400 Bad Request.
    Actual behavior: 201 Created.
    """
    new_body = default_request_body.copy()
    new_body["title"] = 123
    new_body["body"] = True
    new_body["userId"] = "abc"
    response = create_post(base_url, new_body)
    assert response.status_code == 201, "Unexpected status code"
    assert "id" in response.json()


def test_create_post_with_empty_body(base_url, default_request_body):
  """
  API does not validate empty or null fields.
  Expected behavior (real API): 400 Bad Request.
  Actual behavior (jsonplaceholder): 201 Created.
  """
  new_body = default_request_body.copy()
  new_body["title"] = ""
  new_body["body"] = ""
  new_body["userId"] = None
  response = create_post(base_url, new_body)
  assert response.status_code == 201 # BUG: should be 400 (client error)
  assert "id" in response.json()


