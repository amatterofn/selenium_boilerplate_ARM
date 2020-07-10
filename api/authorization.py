import requests

AUTHENTICATION_ENDPOINT = 'https://staging.fiscalnote.com/api/2.0/login'


def get_authorization_header(email, password):
    login_credentials = {
        'email': email,
        'password': password
    }
    login_response = requests.post(AUTHENTICATION_ENDPOINT, json=login_credentials)
    auth_token = login_response.json()['data']['token']

    return {
        'Authorization': f'Token user_token="{auth_token}", user_email="{login_credentials["email"]}"'
    }