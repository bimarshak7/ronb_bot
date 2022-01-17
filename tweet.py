import json
import requests
import os

bearer_token = os.environ['twkey']

def create_url():
    # Replace with user ID below
    user_id = 3141875413 #RONB twitter handle
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def get_params():
    return {'max_results':5}

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    params = get_params()
    res = connect_to_endpoint(url, params)
    #print(json.dumps(res, indent=4, sort_keys=True))
    #tweets=[a['text'].strip() for a in res['data']]
    return res['meta']['newest_id'],res['data']


if __name__ == "__main__":
    main()