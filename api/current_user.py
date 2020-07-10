import requests

CURRENT_USER_ENDPOINT = 'https://staging.fiscalnote.com/api/2.0/current-user'


def get_current_user(authorization_header):
    current_user_response = requests.get(CURRENT_USER_ENDPOINT, headers=authorization_header)
    current_user_data = current_user_response.json()['data']

    return current_user_data