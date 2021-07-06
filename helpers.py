import requests

def get_post_by_id(post_id):
    # Takes in int post_id and returns the post text
    base_url = f"https://jsonplaceholder.typicode.com/posts/"

    if post_id > 100:
        post_id = random.randint(0, 100)
    response = requests.get(f"{base_url}{post_id}")
    assert response.status_code == 200
    return response.json()