import json
import os
import pytest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages import (
    ActionModal,
    ActionsPage,
    ActionSummaryModal,
    ConfirmationModal,
    DeleteActionModal,
    HomePage,
    LoginPage,
    TopSearch
)
from tests import config


def pytest_addoption(parser):
    parser.addoption(
        '--baseurl',
        action='store',
        default='https://www.google.com',
        help='base URL for the application under test'
    )

    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='browser used for testing'
    )

    parser.addoption(
        "--environment",
        action="store",
        default="staging",
        help="environment under test"
    )


def get_driver(desired_browser):
    SELENIUM_GRID_IP_ADDRESS = 'selenium-grid.mgmt.fiscalnote.com'

    if desired_browser == 'chrome':
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
    elif desired_browser == 'firefox':
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
    elif desired_browser == 'chrome-remote':
        driver = webdriver.Remote(
            command_executor=f'http://{SELENIUM_GRID_IP_ADDRESS}:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
    elif desired_browser == 'firefox-remote':
        driver = webdriver.Remote(
            command_executor=f'http://{SELENIUM_GRID_IP_ADDRESS}:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
    else:
        raise Exception('Something really terrible has happened!')

    return driver


@pytest.fixture(scope='session')
def driver(request):
    config.baseurl = request.config.getoption('--baseurl')
    config.browser = request.config.getoption('--browser')
    config.environment = request.config.getoption('--environment')

    _driver = get_driver(config.browser)
    _driver.maximize_window()

    def _quit():
        _driver.quit()

    request.addfinalizer(_quit)

    return _driver


@pytest.fixture(scope='session')
def authenticated_driver(home_page, login_page):
    login_page.login(os.getenv('ENV_USERNAME'), os.getenv('ENV_PASSWORD'))

    assert "Welcome" in home_page.welcome_message


@pytest.fixture(scope='session')
def auth_header(driver):
    ember_simple_auth = json.loads(driver.execute_script('return localStorage.getItem("ember_simple_auth:session");'))
    user_email = ember_simple_auth['authenticated']['userEmail']
    user_token = ember_simple_auth['authenticated']['userToken']

    return {
        'Authorization': f'Token user_token="{user_token}", user_email="{user_email}"'
    }


@pytest.fixture
def action_modal(driver):
    return ActionModal(driver)


@pytest.fixture
def actions_page(driver):
    return ActionsPage(driver)


@pytest.fixture
def actions_summary_modal(driver):
    return ActionSummaryModal(driver)


@pytest.fixture
def confirmation_modal(driver):
    return ConfirmationModal(driver)


@pytest.fixture
def delete_action_modal(driver):
    return DeleteActionModal(driver)


@pytest.fixture(scope='session')
def home_page(driver):
    return HomePage(driver)


@pytest.fixture(scope='session')
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def top_search(driver):
    return TopSearch(driver)
