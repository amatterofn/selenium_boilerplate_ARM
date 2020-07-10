import logging

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from . import locators
from pages.base_page import BasePage


class ActionModal(BasePage):
    @property
    def added_attendees(self):
        return [attendee.text.replace('\n×', '') for attendee in self.find_visible_elements(locators.ATTENDEE, timeout=3)]

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
    def delete_button(self):
        return self.find_visible_element(locators.DELETE_BUTTON)

    @property
    def close_icon(self):
        return self.find_visible_element(locators.CLOSE_ICON)

    @property
    def current_summary_text(self):
        return self.find_visible_element(locators.SUMMARY_SECTION).get_attribute('value')

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
    def end_date_value(self):
        return self.find_visible_element(locators.END_DATE).get_attribute('value')

    @property
    def end_time_value(self):
        return self.find_visible_element(locators.END_TIME).get_attribute('value')

    @property
    def modal_header_text(self):
        return self.find_visible_element(locators.MODAL_HEADER).text

    def add_issue(self, desired_issue):
        issue_input = self.find_visible_element(locators.ISSUE_INPUT)
        logging.info(f'Typing the name of the issue "{desired_issue}"')
        issue_input.send_keys(desired_issue)
        logging.info(f'Selecting typed issue "{desired_issue}"')
        issue = self.find_visible_element(locators.issue_by_issue_text(desired_issue))
        issue.click()

    def add_issues(self, issues):
        for issue in issues:
            self.add_issue(issue)

    def add_label(self, desired_label):
        label_input = self.find_visible_element(locators.LABEL_INPUT)
        logging.info(f'Typing the name of label "{desired_label}"')
        label_input.send_keys(desired_label)
        label = self.find_visible_element(locators.label_by_label_text(desired_label))
        logging.info(f'Selecting typed label "{desired_label}"')
        label.click()

    def add_labels(self, labels):
        for label in labels:
            self.add_label(label)

    def add_linked_item(self, query_text, desired_linked_item):
        linked_item_input = self.find_visible_element(locators.LINKED_ITEM_INPUT)
        logging.info(f'Typing name of linked item "{query_text}"')
        linked_item_input.send_keys(query_text)
        linked_item = self.find_visible_element(locators.linked_item_by_linked_item_text(desired_linked_item))
        logging.info(f'Selecting typed linked item "{desired_linked_item}"')
        linked_item.click()

    def add_attendees(self, query_text, desired_attendee):
        linked_item_input = self.find_visible_element(locators.ATTENDEE_INPUT)
        logging.info(f'Typing name of attendee "{query_text}"')
        linked_item_input.send_keys(query_text)
        linked_item = self.find_visible_element(locators.attendee_by_attendee_text(desired_attendee))
        logging.info(f'Selecting typed attendee "{desired_attendee}"')
        linked_item.click()

    def edit_added_attendees(self, query_text, desired_attendee):
        linked_item_input = self.find_visible_element(locators.ADDED_ATTENDEE_INPUT)
        logging.info(f'Typing name of attendee "{query_text}"')
        linked_item_input.send_keys(query_text)
        linked_item = self.find_visible_element(locators.attendee_by_attendee_text(desired_attendee))
        logging.info(f'Selecting typed attendee "{desired_attendee}"')
        linked_item.click()

    def add_summary(self, desired_summary):
        summary_section = self.find_visible_element(locators.SUMMARY_SECTION)
        logging.info(f'Clearing Summary input')
        summary_section.clear()
        logging.info(f'Adding summary "{desired_summary}"')
        summary_section.send_keys(desired_summary)

    def click_cancel_button(self):
        logging.info('Clicking the Cancel button on the Action Modal.')
        self.cancel_button.click()

    def click_delete_button(self):
        logging.info('Clicking the Delete button on the Action Modal.')
        self.delete_button.click()

    def click_close_icon(self):
        logging.info('Clicking the "X" icon on the Action Modal.')
        self.close_icon.click()

    def click_save_button(self):
        logging.info('Clicking the "Save" button on the Action Modal')
        save_button = self.find_visible_element(locators.SAVE_BUTTON)
        save_button.click()

    def enter_end_date(self, desired_end_date):
        end_date = self.find_visible_element(locators.END_DATE)
        logging.info(f'Clearing end date field and adding "{desired_end_date}"')
        end_date.send_keys(Keys.ENTER)
        end_date.send_keys(desired_end_date)

    def enter_end_time(self, desired_end_time):
        end_time = self.find_visible_element(locators.END_TIME)
        logging.info(f'Clearing end time field and adding "{desired_end_time}"')
        end_time.clear()
        end_time.send_keys(desired_end_time)
        end_time.send_keys(Keys.ENTER)

    def enter_start_date(self, desired_start_date):
        start_date = self.find_visible_element(locators.START_DATE)
        logging.info(f'Clearing start date field and adding "{desired_start_date}"')
        start_date.send_keys(Keys.ENTER)
        start_date.send_keys(desired_start_date)

    def enter_start_time(self, desired_start_time):
        start_time = self.find_visible_element(locators.START_TIME)
        logging.info(f'Clearing start time field and adding "{desired_start_time}"')
        start_time.clear()
        start_time.send_keys(desired_start_time)
        start_time.send_keys(Keys.ENTER)

    def set_action_type(self, desired_action_type):
        logging.info(f'Selecting Action Type drop down and selecting Action Type "{desired_action_type}"')
        select_action_type = Select(self.find_visible_element(locators.SELECT_ACTION_TYPE))
        select_action_type.select_by_visible_text(desired_action_type)

