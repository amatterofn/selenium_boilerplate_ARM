import logging

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from . import locators
from pages.base_page import BasePage


class ActionModal(BasePage):
    @property
    def added_attendees(self):
        return [attendee.text.replace('\n×', '') for attendee in self.find_visible_elements(locators.ATTENDEE)]

    @property
    def added_issues(self):
        return [issue.text for issue in self.find_visible_elements(locators.ISSUE, timeout=3)]

    @property
    def added_labels(self):
        return [label.text for label in self.find_visible_elements(locators.LABEL, timeout=3)]



    @property
    def added_linked_items(self):
        return [linked_item.text.replace('\n×', '') for linked_item in self.find_visible_elements(locators.LINKED_ITEM, timeout=3)]

    @property
    def cancel_button(self):
        return self.find_visible_element(locators.CANCEL_BUTTON)

    @property
    def close_icon(self):
        return self.find_visible_element(locators.CLOSE_ICON)

    @property
    def current_summary_text(self):
        return self.find_visible_element(locators.SUMMARY_SECTION).get_attribute('value')

    @property
    def end_date_value(self):
        return self.find_visible_element(locators.END_DATE).get_attribute('value')

    @property
    def end_time_value(self):
        return self.find_visible_element(locators.END_TIME).get_attribute('value')

    @property
    def is_not_displayed(self):
        return self.is_not_visible(locators.MODAL_HEADER)

    @property
    def is_displayed(self):
        return self.is_visible(locators.MODAL_HEADER)

    @property
    def selected_action_type(self):
        currently_selected = Select(self.find_visible_element(locators.SELECT_ACTION_TYPE)).first_selected_option

        return currently_selected.text.strip()

    @property
    def start_date_value(self):
        return self.find_visible_element(locators.START_DATE).get_attribute('value')

    @property
    def start_time_value(self):
        return self.find_visible_element(locators.START_TIME).get_attribute('value')

    @property
    def modal_header_text(self):
        return self.find_visible_element(locators.MODAL_HEADER).text

    def add_issue(self, desired_issue):
        logging.info('Searching for an Issue')
        issue_input = self.find_visible_element(locators.ISSUE_INPUT)
        issue_input.send_keys(desired_issue)

        logging.info('Selecting an Issue')
        issue = self.find_visible_element(locators.issue_by_issue_text(desired_issue))
        issue.click()

    def add_label(self, desired_label):
        logging.info('Searching for a Label')
        label_input = self.find_visible_element(locators.LABEL_INPUT)
        label_input.send_keys(desired_label)

        logging.info('Selecting a Label')
        label = self.find_visible_element(locators.label_by_label_text(desired_label))
        label.click()

    def add_labels(self, labels):
        for label in labels:
            self.add_label(label)

    def add_issues(self, issues):
        for issue in issues:
            self.add_issue(issue)

    def add_linked_item(self, query_text, desired_linked_item):
        logging.info('Searching for a linked item')
        linked_item_input = self.find_visible_element(locators.LINKED_ITEM_INPUT)
        linked_item_input.send_keys(query_text)

        logging.info('Selecting a linked item')
        linked_item = self.find_visible_element(locators.linked_item_by_linked_item_text(desired_linked_item))
        linked_item.click()

    def add_summary(self, desired_summary):
        logging.info('adding summary text')
        summary_section = self.find_visible_element(locators.SUMMARY_SECTION)
        summary_section.clear()
        summary_section.send_keys(desired_summary)

    def click_cancel_button(self):
        logging.info('clicking cancel button')
        self.cancel_button.click()

    def click_close_icon(self):
        logging.info('Clicking the "X" icon on the Action Modal.')
        self.close_icon.click()

    def click_save_button(self):
        logging.info('clicking save button')
        save_button = self.find_visible_element(locators.SAVE_BUTTON)
        save_button.click()

    def enter_end_date(self, desired_end_date):
        logging.info('Entering an end date')
        end_date = self.find_visible_element(locators.END_DATE)
        end_date.send_keys(Keys.ENTER)
        end_date.send_keys(desired_end_date)

    def enter_end_time(self, desired_end_time):
        logging.info('Entering an end time')
        end_time = self.find_visible_element(locators.END_TIME)
        end_time.clear()
        end_time.send_keys(desired_end_time)
        end_time.send_keys(Keys.ENTER)

    def enter_start_date(self, desired_start_date):
        logging.info('Entering a start date')
        start_date = self.find_visible_element(locators.START_DATE)
        start_date.send_keys(Keys.ENTER)
        start_date.send_keys(desired_start_date)

    def enter_start_time(self, desired_start_time):
        logging.info('Entering a start time time')
        start_time = self.find_visible_element(locators.START_TIME)
        start_time.clear()
        start_time.send_keys(desired_start_time)
        start_time.send_keys(Keys.ENTER)

    def set_action_type(self, desired_action_type):
        logging.info('setting an action type')
        select_action_type = Select(self.find_visible_element(locators.SELECT_ACTION_TYPE))
        select_action_type.select_by_visible_text(desired_action_type)