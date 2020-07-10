from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.wait import wait_for_element_to_be_visible

CLICK_HERE_TO_LOGIN_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.sign-in-form button'
}

EMAIL_INPUT = {
    'by': By.NAME,
    'value': 'email'
}

USERNAME_INPUT = {
    'by': '',
    'value': ''
}

PASSWORD_INPUT = {
    'by': By.NAME,
    'value': 'password'
}

LOGIN_BUTTON = {
    'by': By.CLASS_NAME,
    'value': 'auth0-lock-submit'
}

WELCOME_MESSAGE = {
    'by': By.CSS_SELECTOR,
    'value': 'h1'
}

ADD_ACTION_BUTTON = {
    'by': By.XPATH,
    'value': '//button[text()="+ Add"]'
}

SUMMARY_SECTION = {
    'by': By.CSS_SELECTOR,
    'value': '.summary'
}

ACTION_TYPE_SELECTION = {
    'by': By.CSS_SELECTOR,
    'value': '.action-type'
}

SAVE_BUTTON = {
    'by': By.XPATH,
    'value': '//button[text()="Save"]'
}

SUMMARY_TEXT = {
    'by': By.XPATH,
    'value': '//p[text()="HELLO Professor Marc, I did the homework assignment"]'
}

DELETE_ACTION = {
    'by': By.XPATH,
    'value': '//p[text()="HELLO Professor Marc, I did the homework assignment"]//ancestor::tr//i[@class="ion-trash-b"]'
}

OK_BUTTON = {
    'by': By.XPATH,
    'value': '//button[text()="OK"]'
}

SUMMARY_COLUMN = {
    'by': By.CLASS_NAME,
    'value': 'actions-row__summary-col'
}

CALENDAR_START_DATE_CLEAR = {
    'by': By.ID,
    'value': 'create-action-modal-start-date'
}

CALENDAR_START_DATE_ENTER = {
    'by': By.ID,
    'value': 'create-action-modal-start-date'
}

CALENDAR_START_TIME_CLEAR = {
    'by': By.ID,
    'value': 'create-action-modal-start-time'
}

CALENDAR_START_TIME_ENTER = {
    'by': By.ID,
    'value': 'create-action-modal-start-time'
}

CALENDAR_END_DATE_CLEAR = {
    'by': By.ID,
    'value': 'create-action-modal-end-date'
}

CALENDAR_END_DATE_ENTER = {
    'by': By.ID,
    'value': 'create-action-modal-end-date'
}

CALENDAR_END_TIME_CLEAR = {
    'by': By.ID,
    'value': 'create-action-modal-end-time'
}

CALENDAR_END_TIME_ENTER = {
    'by': By.ID,
    'value': 'create-action-modal-end-time'
}

ATTENDEE_SELECTION = {
    'by': By.ID,
    'value': 'actions-modal__attendees-selectized'
}

ATTENDEE_CLICK = {
    'by': By.XPATH,
    'value': '//div[string()="Farhan Din"]'
}

LINK_SELECTION = {
    'by': By.ID,
    'value': 'linked-items-selectize-selectized'
}

LINK_CLICK = {
    'by': By.XPATH,
    'value': '//div[string()="Revisions Required to identify Actions Placed on Any State Issued License"]'
}


def delete_icon_by_action_summary(action_summary):
    return {
        'by': By.XPATH,
        'value': f'//p[text()="{action_summary}"]//ancestor::tr//i[@class="ion-trash-b"]'
    }


@pytest.mark.homework
def test_user_can_create_a_new_action(driver):
    driver.get('https://staging.fiscalnote.com/?error=notauthorized')

    click_here_to_login_button = wait_for_element_to_be_visible(driver, CLICK_HERE_TO_LOGIN_BUTTON)
    click_here_to_login_button.click()

    email_input = wait_for_element_to_be_visible(driver, EMAIL_INPUT)
    email_input.send_keys('anthony.mattero+1@fiscalnote.com')

    password_input = wait_for_element_to_be_visible(driver, PASSWORD_INPUT)
    password_input.send_keys('B0ssmust@ng')

    login_button = wait_for_element_to_be_visible(driver, LOGIN_BUTTON)
    login_button.click()

    welcome_message = wait_for_element_to_be_visible(driver, WELCOME_MESSAGE)
    assert 'Welcome' in welcome_message.text

    driver.get('https://staging.fiscalnote.com/actions')

    add_action_button = wait_for_element_to_be_visible(driver, ADD_ACTION_BUTTON)
    add_action_button.click()

    summary_section = wait_for_element_to_be_visible(driver, SUMMARY_SECTION)
    summary_section.send_keys('HELLO Professor Marc, I did the homework assignment')

    action_type_selection = Select(wait_for_element_to_be_visible(driver, ACTION_TYPE_SELECTION))
    action_type_selection.select_by_visible_text('Campaign')

    attendee_selection = wait_for_element_to_be_visible(driver, ATTENDEE_SELECTION)
    attendee_selection.send_keys('Farhan Din')

    attendee_click = wait_for_element_to_be_visible(driver, ATTENDEE_CLICK)
    attendee_click.click()

    # link_selection = wait_for_element_to_be_visible(driver, LINK_SELECTION)
    # link_selection.send_keys('Revisions Required to identify Actions Placed on Any State Issued License')
    #
    # link_click = wait_for_element_to_be_visible(driver, LINK_CLICK)
    # link_click.click()
    #
    # sleep(10)

    calendar_start_date_clear = wait_for_element_to_be_visible(driver, CALENDAR_START_DATE_CLEAR)
    calendar_start_date_clear.clear()

    calendar_start_date_enter = wait_for_element_to_be_visible(driver, CALENDAR_START_DATE_ENTER)
    calendar_start_date_enter.send_keys('12/23/2019')

    calendar_start_time_clear = wait_for_element_to_be_visible(driver, CALENDAR_START_TIME_CLEAR)
    calendar_start_time_clear.clear()

    calendar_start_time_enter = wait_for_element_to_be_visible(driver, CALENDAR_START_TIME_ENTER)
    calendar_start_time_enter.send_keys('9:00am')

    calendar_end_date_clear = wait_for_element_to_be_visible(driver, CALENDAR_END_DATE_CLEAR)
    calendar_end_date_clear.clear()

    calendar_end_date_enter = wait_for_element_to_be_visible(driver, CALENDAR_END_DATE_ENTER)
    calendar_end_date_enter.send_keys('12/23/2019')

    calendar_end_time_clear = wait_for_element_to_be_visible(driver, CALENDAR_END_TIME_CLEAR)
    calendar_end_time_clear.clear()

    calendar_end_time_enter = wait_for_element_to_be_visible(driver, CALENDAR_END_TIME_ENTER)
    calendar_end_time_enter.send_keys('5:00pm')

    save_button = wait_for_element_to_be_visible(driver, SAVE_BUTTON)
    save_button.click()

    summary_text = wait_for_element_to_be_visible(driver, SUMMARY_TEXT)
    assert 'HELLO Professor Marc, I did the homework assignment' in summary_text.text

    sleep(5)

    delete_action = wait_for_element_to_be_visible(driver, DELETE_ACTION)
    delete_action.click()

    ok_button = wait_for_element_to_be_visible(driver, OK_BUTTON)
    ok_button.click()

    summary_text = wait_for_element_to_be_visible(driver, SUMMARY_COLUMN)
    assert 'HELLO Professor Marc, I did the homework assignment' not in summary_text.text

    sleep(5)
