from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from .locators import (
    ADD_ACTION_BUTTON,
    END_DATE,
    END_TIME,
    issue_by_issue_text,
    ISSUE_INPUT,
    LABEL_INPUT,
    label_by_label_text,
    LINKED_ITEM_INPUT,
    linked_item_by_linked_item_text,
    SAVE_BUTTON,
    delete_icon_by_action_summary,
    SELECT_ACTION_TYPE,
    START_DATE,
    START_TIME,
    SUMMARY_SECTION
)
from utilities.wait import wait_for_element_to_be_visible


def add_issue(driver, desired_issue):
    issue_input = wait_for_element_to_be_visible(driver, ISSUE_INPUT)
    issue_input.send_keys(desired_issue)

    issue = wait_for_element_to_be_visible(driver, issue_by_issue_text('Agriculture'))
    issue.click()


def add_label(driver, desired_label):
    label_input = wait_for_element_to_be_visible(driver, LABEL_INPUT)
    label_input.send_keys(desired_label)

    label = wait_for_element_to_be_visible(driver, label_by_label_text(desired_label))
    label.click()


def add_linked_item(driver, query_text, desired_linked_item):
    linked_item_input = wait_for_element_to_be_visible(driver, LINKED_ITEM_INPUT)
    linked_item_input.send_keys(query_text)

    linked_item = wait_for_element_to_be_visible(driver, linked_item_by_linked_item_text(desired_linked_item))
    linked_item.click()


def add_summary(driver, desired_summary):
    summary_section = wait_for_element_to_be_visible(driver, SUMMARY_SECTION)
    summary_section.clear()
    summary_section.send_keys(desired_summary)


def click_add_action_button(driver):
    add_action_button = wait_for_element_to_be_visible(driver, ADD_ACTION_BUTTON)
    add_action_button.click()


def click_save_button(driver):
    save_button = wait_for_element_to_be_visible(driver, SAVE_BUTTON)
    save_button.click()


def click_delete_button(driver):
    delete_button = wait_for_element_to_be_visible(driver, delete_icon_by_action_summary)
    delete_button.click()


def enter_end_date(driver, desired_end_date):
    end_date = wait_for_element_to_be_visible(driver, END_DATE)
    end_date.send_keys(Keys.ENTER)
    end_date.send_keys(desired_end_date)


def enter_end_time(driver, desired_end_time):
    end_time = wait_for_element_to_be_visible(driver, END_TIME)
    end_time.clear()
    end_time.send_keys(desired_end_time)
    end_time.send_keys(Keys.ENTER)


def enter_start_date(driver, desired_start_date):
    start_date = wait_for_element_to_be_visible(driver, START_DATE)
    start_date.send_keys(Keys.ENTER)
    start_date.send_keys(desired_start_date)


def enter_start_time(driver, desired_start_time):
    start_time = wait_for_element_to_be_visible(driver, START_TIME)
    start_time.clear()
    start_time.send_keys(desired_start_time)
    start_time.send_keys(Keys.ENTER)


def set_action_type(driver, desired_action_type):
    select_action_type = Select(wait_for_element_to_be_visible(driver, SELECT_ACTION_TYPE))
    select_action_type.select_by_visible_text(desired_action_type)