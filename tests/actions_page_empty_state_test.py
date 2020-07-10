import time
import pytest

from pages.actions_page.page_object import ActionsPage
from pages.home_page.page_object import HomePage
from pages.login_page.page_object import LoginPage


@pytest.mark.actions_page_empty_state
def test_verify_empty_state_action_counts(driver):
    login_page = LoginPage(driver)
    login_page.login('anthony.mattero+automation1@fiscalnote.com', 'B0ssmust@ng')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message
    actions_page = ActionsPage(driver)
    actions_page.navigate()
    assert actions_page.total_actions_count == 0
    assert actions_page.monthly_actions_count == 0
    assert actions_page.weekly_actions_count == 0
    assert "Add Action" in actions_page.empty_state_add_action_button

    time.sleep(3)
