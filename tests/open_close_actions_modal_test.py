import pytest

from datetime import datetime
from random import choice
from selenium.webdriver.common.by import By
from time import sleep

from pages.actions_page.page_object import ActionsPage
from pages.action_modal.page_object import ActionModal
from pages.confirmation_modal.page_object import ConfirmationModal
from pages.home_page.page_object import HomePage
from pages.login_page.page_object import LoginPage
from utilities.wait import wait_for_element_to_be_visible


def delete_icon_by_action_summary(action_summary):
    return {
        'by': By.XPATH,
        'value': f'//p[text()="{action_summary}"]//ancestor::tr//i[@class="ion-trash-b"]'
    }


def new_action_summary(summary_text):
    return {
        'by': By.XPATH,
        'value': f'//td[contains(@class, "actions-row__summary-col")]//p[text()="{summary_text}"]'
    }


def get_random_number():
    return choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def get_date():
    date = datetime.now()

    return f'{date.month}/{date.day}/{date.year}'


def get_timestamp():
    date = datetime.now()

    return f'{date.hour}:{date.minute}:{date.second}'


@pytest.mark.open_close_actions_modal
def test_user_can_open_and_close_actions_modal_with_empty_state_add_action_button(driver):
    login_page = LoginPage(driver)
    login_page.login('anthony.mattero+automation1@fiscalnote.com', 'B0ssmust@ng')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message

    actions_page = ActionsPage(driver)
    actions_page.navigate()
    actions_page.click_empty_state_add_action_button()
    action_modal = ActionModal(driver)
    assert action_modal.modal_header_text == "Add Action"
    assert action_modal.date_is_valid(action_modal.start_date_value) == True
    assert action_modal.time_is_valid(action_modal.start_time_value) == True
    assert action_modal.date_is_valid(action_modal.end_date_value) == True
    assert action_modal.time_is_valid(action_modal.end_time_value) == True
    assert action_modal.action_type_value == 'Meeting'
    assert action_modal.attendee_value == 'Tony Matteros'
