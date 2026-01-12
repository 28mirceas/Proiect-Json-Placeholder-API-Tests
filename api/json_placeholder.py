import requests

def get_posts(base_url, params=None):
    endpoint = f"{base_url}/posts"
    response = requests.get(endpoint, params=params)
    return response


def get_post(base_url, post_id=1):
    endpoint = f"{base_url}/posts/{post_id}"
    response = requests.get(endpoint)
    return response


def create_post(base_url, request_body):
    endpoint = f"{base_url}/posts"
    response = requests.post(endpoint, json=request_body)
    return response


def update_post(base_url, request_body, post_id=1):
    endpoint = f"{base_url}/posts/{post_id}"
    response = requests.put(endpoint, json=request_body)
    return response


def partial_update_post(base_url, request_body, post_id=1):
    endpoint = f"{base_url}/posts/{post_id}"
    response = requests.patch(endpoint, json=request_body)
    return response


def delete_post(base_url, post_id=1):
    endpoint = f"{base_url}/posts/{post_id}"
    response = requests.delete(endpoint)
    return response
