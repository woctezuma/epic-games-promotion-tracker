import requests

GRAPHQL_API_URL = "https://graphql.epicgames.com/graphql"


def send_post_request_to_api(json_data, verbose=True):
    r = requests.post(GRAPHQL_API_URL, json=json_data)
    return to_data(r, verbose=verbose)


def to_data(response, verbose=True):
    if response.ok:
        data = response.json()
    else:
        data = None
        if verbose:
            print(f"Status code = {response.status_code}")
    return data
