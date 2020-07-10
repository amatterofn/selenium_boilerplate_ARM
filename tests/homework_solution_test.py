import logging
import pytest
import requests
import unittest

from time import sleep
from datetime import datetime, timedelta
from random import choice
from selenium.webdriver.common.by import By

from pages import ActionModal, ActionsPage, ActionsSummaryModal, ConfirmationModal, HomePage, LoginPage, TopSearch

from api import authorization, actions, current_user, issues
from utilities.validators import date_is_valid, time_is_valid
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


def get_date_future(days_in_future=1):
    dt = datetime.now()
    td = timedelta(days=days_in_future)
    future_date = dt + td
    return f'{future_date.month}/{future_date.day}/{future_date.year}'


def get_timestamp():
    date = datetime.now()

    return f'{date.hour}:{date.minute}:{date.second}'


def test_action_counts_for_empty_state(login_page, home_page, actions_page):

    login_page.login('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()

    assert actions_page.total_actions_count == 0
    assert actions_page.actions_this_week_count == 0
    assert actions_page.actions_this_month_count == 0

    assert "No actions yet." in actions_page.empty_state_help_text
    assert "Create one to record meetings, calls, and other actions to share past and future activity with your team." in actions_page.empty_state_help_text

    assert actions_page.empty_state_add_action_button.is_displayed()


def test_user_can_open_and_close_actions_modal_with_empty_state_add_action_button_and_close_it_with_cancel_button(
        login_page, home_page, actions_page, action_modal, confirmation_modal):

    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.delete_all_actions(auth_header)

    login_page.login('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')

    welcome_message = "Welcome, Anthony"
    logging.info(f'Verifying that the text "{welcome_message}" appears in the welcome message on the Home Page.')
    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()
    actions_page.click_empty_state_add_action_button()

    logging.info('Verifying Action Modal is visible.')
    assert action_modal.modal_header_text == "Add Action"
    logging.info('Verifying Action Modal start date is visible and valid.')
    assert date_is_valid(action_modal.start_date_value)
    logging.info('Verifying Action Modal start time is visible and valid.')
    assert time_is_valid(action_modal.start_time_value)
    logging.info('Verifying Action Modal end date is visible and valid.')
    assert date_is_valid(action_modal.end_date_value)
    logging.info('Verifying Action Modal end time is visible and valid.')
    assert time_is_valid(action_modal.end_time_value)
    selected_action_type = "Meeting"
    logging.info(f'Verifying Action Modal action type is "{selected_action_type}"')
    assert action_modal.selected_action_type == "Meeting"
    added_attendees = "Anthony Mattero"
    logging.info(f'Verifying Action Modal Attendee is "{added_attendees}"')
    assert action_modal.added_attendees == ['Anthony Mattero']
    logging.info('Verifying Action Modal Linked Items are NULL')
    assert action_modal.added_linked_items == []
    logging.info('Verifying Action Modal Labels are NULL')
    assert action_modal.added_labels == []
    logging.info('Verifying Action Modal Issues are NULL')
    assert action_modal.added_issues == []
    logging.info('Verifying Action Modal Summary is NULL')
    assert action_modal.current_summary_text == ''

    action_modal.click_cancel_button()

    logging.info('Verifying Confirmation Modal is visible.')
    assert confirmation_modal.is_displayed
    confirmation_modal.click_cancel_button()
    logging.info('Verifying Confirmation Modal is not visible.')
    assert confirmation_modal.is_not_displayed
    logging.info('Verifying Action Modal is still visible.')
    assert action_modal.is_displayed

    action_modal.click_cancel_button()
    logging.info('Verifying Confirmation Modal is visible.')
    assert confirmation_modal.main_is_displayed
    confirmation_modal.click_confirm_button()
    logging.info('Verifying Confirmation Modal is not visible.')
    assert confirmation_modal.is_not_displayed
    logging.info('Verifying Action Modal is no longer visible.')
    assert action_modal.is_not_displayed


def test_user_can_open_and_close_actions_modal_with_main_add_action_button_and_close_it_with_x_icon(
        login_page, home_page, actions_page, action_modal, confirmation_modal):

    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.delete_all_actions(auth_header)

    login_page.login('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')

    welcome_message = "Welcome, Anthony"
    logging.info(f'Verifying that the text "{welcome_message}" appears in the welcome message on the Home Page.')
    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()
    actions_page.click_empty_state_add_action_button()

    logging.info('Verifying Action Modal is visible.')
    assert action_modal.modal_header_text == "Add Action"
    logging.info('Verifying Action Modal start date is visible and valid.')
    assert date_is_valid(action_modal.start_date_value)
    logging.info('Verifying Action Modal start time is visible and valid.')
    assert time_is_valid(action_modal.start_time_value)
    logging.info('Verifying Action Modal end date is visible and valid.')
    assert date_is_valid(action_modal.end_date_value)
    logging.info('Verifying Action Modal end time is visible and valid.')
    assert time_is_valid(action_modal.end_time_value)
    selected_action_type = "Meeting"
    logging.info(f'Verifying Action Modal action type is "{selected_action_type}"')
    assert action_modal.selected_action_type == "Meeting"
    added_attendees = "Anthony Mattero"
    logging.info(f'Verifying Action Modal Attendee is "{added_attendees}"')
    assert action_modal.added_attendees == ['Anthony Mattero']
    logging.info('Verifying Action Modal Linked Items are NULL')
    assert action_modal.added_linked_items == []
    logging.info('Verifying Action Modal Labels are NULL')
    assert action_modal.added_labels == []
    logging.info('Verifying Action Modal Issues are NULL')
    assert action_modal.added_issues == []
    logging.info('Verifying Action Modal Summary is NULL')
    assert action_modal.current_summary_text == ''

    action_modal.click_close_icon()

    logging.info('Verifying Confirmation Modal is visible.')
    assert confirmation_modal.is_displayed
    confirmation_modal.click_cancel_button()
    logging.info('Verifying Confirmation Modal is not visible.')
    assert confirmation_modal.is_not_displayed
    logging.info('Verifying Action Modal is still visible.')
    assert action_modal.is_displayed

    action_modal.click_close_icon()
    logging.info('Verifying Confirmation Modal is visible.')
    assert confirmation_modal.main_is_displayed
    confirmation_modal.click_confirm_button()
    logging.info('Verifying Confirmation Modal is not visible.')
    assert confirmation_modal.is_not_displayed
    logging.info('Verifying Action Modal is no longer visible.')
    assert action_modal.is_not_displayed


def test_user_can_create_a_new_action(login_page, home_page, actions_page):
    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.delete_all_actions(auth_header)

    login_page.login('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()
    # actions_page.click_add_action_button()

    # action_modal = ActionModal(driver)
    # action_modal.enter_start_date('8/14/2019')
    # action_modal.enter_start_time('6:00am')
    # action_modal.enter_end_date('8/14/2019')
    # action_modal.enter_end_time('5:00pm')
    # action_modal.set_action_type('Phone Call')
    # action_modal.add_linked_item('US HR 1478', 'US - HR 1478')
    # action_modal.add_labels(('agriculture', 'Farming', 'welfare'))
    # action_modal.add_issue('Agriculture')
    # assert action_modal.added_labels == ['agriculture']
    # assert action_modal.added_issues == ['Agriculture']
    #
    # action_summary_text = f'{get_date()} {get_timestamp()} - Summary created by Tony Mattero.'
    # action_modal.add_summary(action_summary_text)
    #
    # action_modal.click_save_button()
    #
    # new_action = wait_for_element_to_be_visible(driver, new_action_summary(action_summary_text))
    # assert new_action.is_displayed()
    #
    # delete_icon = wait_for_element_to_be_visible(driver, delete_icon_by_action_summary(action_summary_text))
    # delete_icon.click()
    #
    # confirmation_modal = ConfirmationModal(driver)
    # confirmation_modal.click_ok_button()

    # expected_action_1_start = "Mar 27, 2020 2:08 PM"
    # logging.info(f'Verifying that the "Start" value for the action in position 1 equals "{expected_action_1_start}"')
    # assert actions_page.get_action_start_by_position(1) == expected_action_1_start
    #
    # expected_action_1_end = "Mar 27, 2020 3:08 PM"
    # logging.info(f'Verifying that the "End" value for the action in position 1 equals "{expected_action_1_end}"')
    # assert actions_page.get_action_end_by_position(1) == expected_action_1_end
    #
    # expected_action_2_start = "Mar 27, 2020 2:08 PM"
    # logging.info(f'Verifying that the "Start" value for the action in position 2 equals "{expected_action_2_start}"')
    # assert actions_page.get_action_start_by_position(2) == expected_action_2_start
    #
    # expected_action_2_end = "Mar 27, 2020 3:08 PM"
    # logging.info(f'Verifying that the "End" value for the action in position 2 equals "{expected_action_2_end}"')
    # assert actions_page.get_action_end_by_position(2) == expected_action_2_end
    #
    # expected_action_3_start = "Mar 4, 2020 2:08 PM"
    # logging.info(f'Verifying that the "Start" value for the action in position 3 equals "{expected_action_3_start}"')
    # assert actions_page.get_action_start_by_position(3) == expected_action_3_start
    #
    # expected_action_3_end = "Mar 5, 2020 3:08 PM"
    # logging.info(f'Verifying that the "End" value for the action in position 3 equals "{expected_action_3_end}"')
    # assert actions_page.get_action_end_by_position(3) == expected_action_3_end

    expected_creator = 'Tem Automation'
    logging.info(f'Verifying that the "Creator" value for the action in position 1 equals "{expected_creator}"')
    assert actions_page.get_action_creator_by_position(1) == expected_creator

    expected_attendees = ['Herm Automation', 'Selenium Course', 'Tem Automation']
    logging.info(f'Verifying that the "Attendees" value for the action in position 1 equals "{expected_attendees}"')
    assert actions_page.get_action_attendees_by_position(1) == expected_attendees

    expected_linked_items = ['US - HR 1', 'GA - SB 507']
    logging.info(f'Verifying that the linked items values for the action in position 1 equals "{expected_linked_items}"')
    assert actions_page.get_action_linked_items_by_position(1) == expected_linked_items

    expected_issues = ['Agriculture', 'Farming', 'Welfare']
    logging.info(f'Verifying that the issue values for the action in position 1 equals "{expected_issues}"')
    assert actions_page.get_action_issues_by_position(1) == expected_issues

    expected_summary = 'Edit summary and find the position'
    logging.info(f'Verifying that the "Summary" value for the action in position 1 equals "{expected_summary}"')
    assert actions_page.get_action_summary_by_position(1) == expected_summary


def test_user_can_add_future_action_state_federal_legislator(login_page, home_page, actions_page, action_modal):
    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.delete_all_actions(auth_header)

    login_page.login('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()
    actions_page.click_add_action_button()

    action_modal.enter_start_date(get_date_future())
    action_modal.enter_start_time('6:00am')
    action_modal.enter_end_date(get_date_future())
    action_modal.enter_end_time('5:00pm')
    action_modal.set_action_type('Fundraiser')
    action_modal.add_attendees('selenium course', 'Selenium Course')
    action_modal.add_linked_item('john davis', 'OR - John Davis')
    action_modal.add_linked_item('todd young', 'US - Todd Young')
    action_modal.add_labels(('agriculture', 'farming', 'welfare'))
    action_modal.add_issues(('Agriculture', 'Farming', 'Welfare'))

    action_summary_text = f'This is a future action with linked items for federal and state legislators.'
    action_modal.add_summary(action_summary_text)

    action_modal.click_save_button()

    expected_summary = 'This is a future action with linked items for federal and state legislators.'
    logging.info(f'Verifying that the "Summary" value for the action in position 1 equals "{expected_summary}"')
    assert actions_page.get_action_summary_by_position(1) == expected_summary

    logging.info(f'Clicking the edit button for the newly created action')
    actions_page.click_action_edit_button_by_position(1)
    logging.info('Verifying Action Modal is visible.')
    assert action_modal.modal_header_text == "Edit Action"
    added_start_date = get_date_future()
    logging.info(f'Verifying Action Modal start date is "{added_start_date}"')
    assert action_modal.start_date_value == added_start_date
    added_start_time = '6:00am'
    logging.info(f'Verifying Action Modal start time is "{added_start_time}"')
    assert action_modal.start_time_value == added_start_time
    added_end_date = get_date_future()
    logging.info(f'Verifying Action Modal end date is "{added_end_date}"')
    assert action_modal.end_date_value == added_end_date
    added_end_time = '5:00pm'
    logging.info(f'Verifying Action Modal end time is "{added_end_time}"')
    assert action_modal.end_time_value == added_end_time
    selected_action_type = "Fundraiser"
    logging.info(f'Verifying Action Modal action type is "{selected_action_type}"')
    assert action_modal.selected_action_type == selected_action_type
    added_attendees = ['Anthony Mattero', 'Selenium Course']
    logging.info(f'Verifying Action Modal Attendees are "{added_attendees}"')
    assert action_modal.added_attendees == added_attendees
    added_linked_items = ['OR - John Davis', 'US - Todd Young']
    logging.info(f'Verifying Action Modal Linked Items are "{added_linked_items}"')
    assert action_modal.added_linked_items == added_linked_items
    added_labels = ['agriculture', 'farming', 'welfare']
    logging.info(f'Verifying Action Modal Labels are "{added_labels}"')
    assert action_modal.added_labels == added_labels
    added_issues = ['Agriculture', 'Welfare', 'Farming']
    logging.info(f'Verifying Action Modal Labels are "{added_issues}"')
    assert action_modal.added_issues == added_issues
    current_summary_text = 'This is a future action with linked items for federal and state legislators.'
    logging.info(f'Verifying the Action Modal Summary text is "{current_summary_text}"')
    assert action_modal.current_summary_text == current_summary_text
    sleep(3)

    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.delete_all_actions(auth_header)


def test_user_can_edit_an_existing_action(login_page, home_page, actions_page, action_modal):
    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.delete_all_actions(auth_header)

    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.create_action(auth_header)

    login_page.login('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()

    logging.info(f'Clicking the edit button for the newly created action')
    actions_page.click_action_edit_button_by_position(1)
    logging.info('Verifying Action Modal is visible.')
    assert action_modal.modal_header_text == "Edit Action"

    action_modal.enter_start_date(get_date_future())
    action_modal.enter_start_time('6:00am')
    action_modal.enter_end_date(get_date_future())
    action_modal.enter_end_time('5:00pm')
    action_modal.set_action_type('Testimony')
    action_modal.edit_added_attendees('selenium course', 'Selenium Course')
    action_modal.add_linked_item('john davis', 'OR - John Davis')
    action_modal.add_linked_item('todd young', 'US - Todd Young')
    action_modal.add_labels(('agriculture', 'farming', 'welfare'))
    action_modal.add_issues(('Agriculture', 'Farming', 'Welfare'))
    action_summary_text = f'This is an edited action.'
    action_modal.add_summary(action_summary_text)

    action_modal.click_save_button()

    expected_summary = 'This is an edited action.'
    logging.info(f'Verifying that the "Summary" value for the action in position 1 equals "{expected_summary}"')
    assert actions_page.get_action_summary_by_position(1) == expected_summary
    logging.info(f'Clicking the edit button for the newly created action')
    actions_page.click_action_edit_button_by_position(1)
    logging.info('Verifying Action Modal is visible.')
    assert action_modal.modal_header_text == "Edit Action"
    added_start_date = get_date_future()
    logging.info(f'Verifying Action Modal start date is "{added_start_date}"')
    assert action_modal.start_date_value == added_start_date
    added_start_time = '6:00am'
    logging.info(f'Verifying Action Modal start time is "{added_start_time}"')
    assert action_modal.start_time_value == added_start_time
    added_end_date = get_date_future()
    logging.info(f'Verifying Action Modal end date is "{added_end_date}"')
    assert action_modal.end_date_value == added_end_date
    added_end_time = '5:00pm'
    logging.info(f'Verifying Action Modal end time is "{added_end_time}"')
    assert action_modal.end_time_value == added_end_time
    selected_action_type = "Testimony"
    logging.info(f'Verifying Action Modal action type is "{selected_action_type}"')
    assert action_modal.selected_action_type == selected_action_type
    added_attendees = ['Anthony Mattero', 'Selenium Course']
    logging.info(f'Verifying Action Modal Attendees are "{added_attendees}"')
    assert action_modal.added_attendees == added_attendees
    added_linked_items = ['OR - John Davis', 'US - Todd Young']
    logging.info(f'Verifying Action Modal Linked Items are "{added_linked_items}"')
    assert action_modal.added_linked_items == added_linked_items
    added_labels = ['agriculture', 'farming', 'welfare']
    logging.info(f'Verifying Action Modal Labels are "{added_labels}"')
    assert action_modal.added_labels == added_labels
    added_issues = ['Agriculture', 'Farming', 'Welfare']
    logging.info(f'Verifying Action Modal Labels are "{added_issues}"')
    assert action_modal.added_issues == added_issues
    current_summary_text = 'This is an edited action.'
    logging.info(f'Verifying the Action Modal Summary text is "{current_summary_text}"')
    assert action_modal.current_summary_text == current_summary_text
    sleep(3)

    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.delete_all_actions(auth_header)

# def test_api():
#     login_credentials = {
#         'email': 'anthony.mattero+selenium@fiscalnote.com',
#         'password': 'B0ssmust@ng8'
#     }
#
#     auth_header = authorization.get_authorization_header(login_credentials['email'], login_credentials['password'])
#     actions.create_action(auth_header, action_type= 'Roundtable', summary= 'Marc is learnding me')


def test_user_can_delete_action(login_page, home_page, actions_page, confirmation_modal):
    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.delete_all_actions(auth_header)
    action = actions.create_action(auth_header, summary='This action needs to be deleted.')

    login_page.login('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()

    expected_actions_count = 1
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    actions_page.click_delete_action_icon_by_position(1)

    logging.info('Verifying that the "Delete Action" modal is visible.')
    assert confirmation_modal.is_displayed
    assert confirmation_modal.modal_title == 'Delete Action'

    confirmation_modal.click_cancel_button()

    logging.info('Verifying that the "Delete Action" modal is not visible.')
    assert confirmation_modal.is_not_displayed

    logging.info('Verifying that the action in position 1 has a summary of "This action needs to be deleted."')
    assert actions_page.get_action_summary_by_position(1) == 'This action needs to be deleted.'

    actions_page.click_delete_action_icon_by_position(1)
    confirmation_modal.click_ok_button()

    expected_actions_count = 0
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count


def test_user_can_batch_delete_actions(login_page, home_page, actions_page, confirmation_modal):
    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.delete_all_actions(auth_header)

    for number in range(1, 11):
        actions.create_action(auth_header, summary=f'Action #{number}')

    login_page.login('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()

    expected_actions_count = 10
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    actions_page.select_all_actions_on_current_page()

    logging.info('Verifying that 10 actions are selected.')
    assert actions_page.selected_count == '10 Selected'

    actions_page.click_delete_button()

    logging.info('Verifying that the "Delete Action" modal is visible.')
    assert confirmation_modal.main_is_displayed
    assert confirmation_modal.modal_title == 'Delete Action'

    confirmation_modal.click_cancel_button()

    actions_page.click_delete_button()

    logging.info('Verifying that the "Delete Action" modal is visible.')
    assert confirmation_modal.main_is_displayed
    assert confirmation_modal.modal_title == 'Delete Action'

    confirmation_modal.click_ok_button()

    expected_actions_count = 0
    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that the "Total Actions" count equals {expected_actions_count}.')
    assert expected_actions_count == actual_actions_count

    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    logging.info('Refreshing Actions Center Page')
    # driver.refresh()
    actions_page.driver.refresh()

    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that the "Total Actions" count equals {expected_actions_count}.')
    assert expected_actions_count == actual_actions_count

    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    sleep(2)


def test_user_can_batch_delete_individual_actions(login_page, home_page, actions_page, confirmation_modal, driver):
    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.delete_all_actions(auth_header)

    for number in range(10, 0, -1):
        actions.create_action(auth_header, summary=f'Action #{number}')

    login_page.login('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()

    expected_actions_count = 10
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    positions = list(range(1, 11))
    deleted_action_positions = []

    for iteration in range(3):
        position = choice(positions)
        positions.remove(position)
        actions_page.select_action_by_position(position)
        deleted_action_positions.append(position)

    actions_page.click_delete_button()

    confirmation_modal.click_ok_button()

    expected_actions_count = 7
    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that the "Total Actions" count equals {expected_actions_count}.')
    assert expected_actions_count == actual_actions_count

    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    logging.info('Refreshing Actions Center Page')
    driver.refresh()

    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that the "Total Actions" count equals {expected_actions_count}.')
    assert expected_actions_count == actual_actions_count

    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    expected_action_summaries = [f'Action #{position}' for position in positions]
    logging.info(f'Verifying that the following actions are visible: {expected_action_summaries}')
    assert actions_page.visible_action_summaries == expected_action_summaries

    driver.refresh()

    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that the "Total Actions" count equals {expected_actions_count}.')
    assert expected_actions_count == actual_actions_count

    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    logging.info(f'Verifying that the following actions are visible: {expected_action_summaries}')
    assert actions_page.visible_action_summaries == expected_action_summaries


def test_user_can_search_for_actions_by_action_summary(login_page, home_page, actions_page, top_search):
    auth_header = authorization.get_authorization_header('selenium.course@fiscalnote.com', 'Meatball1!!')
    actions.delete_all_actions(auth_header)

    action_summaries = [
        'this action summary is unique',
        'this action summary is the same',
        'this action summary is the same'
    ]

    for action_summary in action_summaries:
        actions.create_action(auth_header, summary=action_summary)

    login_page.login('selenium.course@fiscalnote.com', 'Meatball1!!')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()

    expected_actions_count = 3
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    expected_visible_actions = list(reversed(action_summaries))
    logging.info(f'Verifying that the following actions are visible: {expected_visible_actions}')
    assert actions_page.visible_action_summaries == expected_visible_actions

    top_search.perform_search('unique')

    expected_actions_count = 1
    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count

    expected_action_summaries = ['this action summary is unique']
    logging.info(f'Verifying that the following actions are visible: {expected_action_summaries}')
    assert actions_page.visible_action_summaries == expected_action_summaries

    top_search.perform_search('same')

    expected_actions_count = 2
    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count

    expected_action_summaries = [
        'this action summary is the same',
        'this action summary is the same'
    ]
    logging.info(f'Verifying that the following actions are visible: {expected_action_summaries}')
    assert actions_page.visible_action_summaries == expected_action_summaries

    top_search.perform_search('this_should_not_match_anything')

    expected_actions_count = 0
    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count

    expected_action_summaries = []
    logging.info(f'Verifying that the following actions are visible: {expected_action_summaries}')
    assert actions_page.visible_action_summaries == expected_action_summaries

    sleep(5)


def test_user_can_open_actions_summary_modal(actions_page, home_page, login_page, actions_summary_modal):
    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.delete_all_actions(auth_header)

    logging.info('Creating 5 past actions')
    for number in range(5):
        actions.create_action(
            auth_header,
            end_date=datetime.now() - timedelta(days=7),
            start_date=datetime.now() - timedelta(days=7, hours=1),
            summary='past action'
        )

    logging.info('Creating 10 current actions')
    for number in range(10):
        actions.create_action(auth_header, summary='current action')

    logging.info('Creating 5 future actions')
    for number in range(5):
        actions.create_action(
            auth_header,
            end_date=datetime.now() + timedelta(days=7),
            start_date=datetime.now() + timedelta(days=7, hours=1),
            summary='future action')

    login_page.login('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()

    actions_page.click_see_actions_summary_link()

    logging.info('Verifying Actions Summary Modal is visible.')
    assert actions_summary_modal.modal_header_text == "Actions Summary"

    expected_total_actions_count = 20
    logging.info(f'Verifying a count of {expected_total_actions_count} total actions.')
    assert actions_summary_modal.total_actions_count == expected_total_actions_count

    logging.info(f'Verify that "Total Actions" in the modal match the page count.')
    assert actions_summary_modal.total_actions_count == expected_total_actions_count

    expected_monthly_actions_count = 20
    logging.info(f'Verifying a count of {expected_monthly_actions_count} monthly actions.')
    assert actions_summary_modal.actions_this_month_count == expected_monthly_actions_count

    logging.info(f'Verify that "Monthly Actions" in the modal match the page count.')
    assert actions_summary_modal.actions_this_month_count == expected_total_actions_count

    expected_weekly_actions_count = 10
    logging.info(f'Verifying a count of {expected_weekly_actions_count} weekly actions.')
    assert actions_summary_modal.actions_this_week_count == expected_weekly_actions_count

    logging.info(f'Verify that "Weekly Actions" in the modal match the page count.')
    assert actions_summary_modal.actions_this_week_count == expected_total_actions_count

    sleep(2)


def test_uer_can_load_more_actions(actions_page, home_page, login_page):

    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.delete_all_actions(auth_header)

    logging.info('Creating 40 actions.')
    for number in range(1, 41):
        actions.create_action(auth_header, summary=f'Summary #{number}')

    login_page.login('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()

    expected_actions_count = 40
    actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count

    actions_page.load_more_actions()

    expected_actions_count = 40
    actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count

    actions_page.load_more_actions()

    expected_actions_count = 40
    actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count


def test_user_can_filter_by_start_and_end_date_to_find_past_actions(actions_page, home_page, login_page):
    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.delete_all_actions(auth_header)

    logging.info('Creating 5 past actions.')
    for number in range(5):
        actions.create_action(
            auth_header,
            end_date=datetime.now() - timedelta(days=7),
            start_date=datetime.now() - timedelta(days=7, hours=1),
            summary='past action'
        )

    logging.info('Creating 10 actions on current day.')
    for number in range(10):
        actions.create_action(auth_header, summary='current date')

    logging.info('Creating 5 future actions.')
    for number in range(5):
        actions.create_action(
            auth_header,
            end_date=datetime.now() + timedelta(days=7, hours=1),
            start_date=datetime.now() + timedelta(days=7),
            summary='future action'
        )

    login_page.login('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()

    expected_actions_count = 15
    actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count

    actions_page.open_filter_by_filter_text("Start")
    actions_page.move_calendar_widget_back('start')
    actions_page.click_date('start', '21')
    actions_page.click_date_filter_apply_button('start')

    actions_page.open_filter_by_filter_text("End")
    actions_page.move_calendar_widget_back('end')
    actions_page.click_date('end', '27')
    actions_page.click_date_filter_apply_button('end')

    sleep(5)


def test_user_can_create_action(driver):
    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    actions.create_action(auth_header)


def test_user_can_create_issue(driver):
    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    issues.create_issue(auth_header, name='Tony Created This Issue')


@pytest.mark.api
def test_user_can_delete_all_issues():
    auth_header = authorization.get_authorization_header('anthony.mattero+selenium@fiscalnote.com', 'B0ssmust@ng8')
    logging.info(actions.get_all_actions(auth_header))


def test_api():
    auth_header = authorization.get_authorization_header('selenium.course@fiscalnote.com', '')
    user = current_user.get_current_user(auth_header)

    # action = actions.create_action(auth_header, action_type='Roundtable', summary='This is a custom summary.')

    for number in range(1, 11):
        actions.create_action(auth_header, summary=f'Action #{number}')

    actions.delete_all_actions(auth_header)
