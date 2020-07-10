import json
import logging
import pytest
import requests

from time import sleep

from pages.home_page.page_object import HomePage
from pages.login_page.page_object import LoginPage


@pytest.mark.local_storage
def test_local_storage(driver):
    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'not_my_real_password')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message

    ember_simple_auth = json.loads(driver.execute_script('return localStorage.getItem("ember_simple_auth:session");'))
    auth_token = ember_simple_auth['authenticated']['userToken']
    headers = {
        'Authorization': f'Token user_token="{auth_token}", user_email="selenium.course@fiscalnote.com"'
    }

    current_user_response = requests.get('https://staging.fiscalnote.com/api/2.0/current-user', headers=headers)
    logging.info(current_user_response.json())

    driver.get('https://staging.fiscalnote.com/issues')

    current_user_response = requests.get('https://staging.fiscalnote.com/api/2.0/current-user', headers=headers)
    logging.info(current_user_response.json())

    sleep(5)

    driver.get('https://staging.fiscalnote.com/actions')

    current_user_response = requests.get('https://staging.fiscalnote.com/api/2.0/current-user', headers=headers)
    logging.info(current_user_response.json())

    sleep(5)

    driver.get('https://staging.fiscalnote.com/mailing-lists')

    current_user_response = requests.get('https://staging.fiscalnote.com/api/2.0/current-user', headers=headers)
    logging.info(current_user_response.json())

    sleep(5)