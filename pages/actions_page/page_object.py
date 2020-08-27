import logging

from . import locators
from pages.base_page import BasePage


class ActionsPage(BasePage):
    @property
    def actions_this_month_count(self):
        return int(self.find_visible_element(locators.action_count_by_description('This Month')).text)

    @property
    def actions_this_week_count(self):
        return int(self.find_visible_element(locators.action_count_by_description('This Week')).text)

    @property
    def delete_button(self):
        return self.find_visible_element(locators.DELETE_BUTTON)

    @property
    def empty_state_add_action_button(self):
        return self.find_visible_element(locators.EMPTY_STATE_ADD_ACTION_BUTTON)

    @property
    def empty_state_help_text(self):
        return self.find_visible_element(locators.EMPTY_STATE_HELP_TEXT).text

    @property
    def see_actions_summary_link(self):
        return self.find_visible_element(locators.SEE_ACTIONS_SUMMARY_LINK)

    @property
    def selected_count(self):
        return self.find_visible_element(locators.SELECTED_COUNT).text

    @property
    def total_actions_count(self):
        return int(self.find_visible_element(locators.action_count_by_description('Total')).text)

    @property
    def visible_action_summaries(self):
        return [action_summary.text for action_summary in self.find_visible_elements(locators.ACTION_SUMMARY)]

    @property
    def visible_actions_count(self):
        return len(self.find_visible_elements(locators.ACTION_CONTAINER, timeout=5))

    def click_add_action_button(self):
        logging.info('Clicking main "Add Action" button.')
        add_action_button = self.find_visible_element(locators.ADD_ACTION_BUTTON)
        add_action_button.click()

    def click_date(self, end_or_start, desired_date):
        logging.info(f'Click the date with text "{desired_date}" in the calendar widget.')
        self.find_visible_element(locators.date_by_date_text(end_or_start, desired_date)).click()

    def click_date_filter_apply_button(self, end_or_start):
        logging.info(f'Clicking the "Apply" button for the "{end_or_start}" filter.')
        self.find_visible_element(locators.date_filter_apply_button(end_or_start)).click()

    def click_delete_button(self):
        logging.info('Clicking "Delete" button.')
        self.delete_button.click()

    def click_empty_state_add_action_button(self):
        logging.info('Clicking empty state "Add Action" button.')
        self.empty_state_add_action_button.click()

    def click_delete_action_icon_by_position(self, position):
        logging.info(f'Clicking the delete icon for action in position {position}.')
        self.find_visible_element(locators.delete_action_icon_by_position(position)).click()

    def click_see_actions_summary_link(self):
        logging.info('Clicking "See actions summary" link.')
        self.see_actions_summary_link.click()

    def get_action_attendees_by_position(self, position):
        attendee_elements = [
            attendee for attendee in self.find_present_elements(locators.action_attendees_by_position(position))
        ]

        return [attendee.get_attribute('innerText').strip() for attendee in attendee_elements]

    def get_action_creator_by_position(self, position):
        return self.find_present_element(locators.action_creator_by_position(position)).get_attribute('innerText').strip()

    def get_action_end_by_position(self, position):
        return self.find_visible_element(locators.action_end_by_position(position)).text.replace('\n', ' ')

    def get_action_issues_by_position(self, position):
        return [issue.get_attribute('innerText').strip() for issue in self.find_present_elements(locators.action_issues_by_position(position))]

    def get_action_start_by_position(self, position):
        return self.find_visible_element(locators.action_start_by_position(position)).text.replace('\n', ' ')

    def get_action_summary_by_position(self, position):
        return self.find_present_element(locators.action_summary_by_position(position)).get_attribute('innerText').strip()

    def navigate(self):
        actions_page_url = 'https://staging.fiscalnote.com/actions'
        logging.info(f'Navigating to {actions_page_url}')
        self.driver.get(actions_page_url)

    def load_more_actions(self):
        logging.info('Loading more actions.')
        self.move_to_element(locators.LOAD_MORE)

    def move_calendar_widget_back(self, end_or_start):
        logging.info('Moving calendar widget to previous month.')

        # Was previously using .ion-chevron-left here. Switched to a parent locator of .pmu-prev
        self.find_present_element(locators.date_filter_previous_next(end_or_start, 'prev')).click()

    def move_calendar_widget_forward(self, end_or_start):
        logging.info('Moving calendar widget to next month.')

        # Was previously using .ion-chevron-left here. Switched to a parent locator of .pmu-next
        self.find_present_element(locators.date_filter_previous_next(end_or_start, 'next')).click()

    def open_filter_by_filter_text(self, filter_text):
        logging.info(f'Opening filter with text "{filter_text}."')
        self.find_visible_element(locators.actions_filter_by_filter_text(filter_text)).click()

    def select_action_by_action_summary(self, action_summary):
        logging.info(f'Clicking checkbox for action with summary "{action_summary}"')
        self.find_visible_element(locators.action_checkbox_by_action_summary(action_summary)).click()

    def select_action_by_position(self, position):
        logging.info(f'Clicking checkbox for action in {position}.')
        self.find_visible_element(locators.action_checkbox_by_position(position)).click()

    def select_all_actions_on_current_page(self):
        logging.info('Clicking on select dropdown.')
        self.find_visible_element(locators.SELECT_DROPDOWN).click()

        logging.info('Click the "Select all on current page" option.')
        self.find_visible_element(locators.select_dropdown_option_by_option_text('Select all on current page')).click()

    def wait_for_visible_actions_count_to_equal(self, expected_actions_count):
        return self.wait_for_number_of_elements_to_be_visible(locators.ACTION_CONTAINER, expected_actions_count)

    def wait_for_total_actions_count_to_equal(self, expected_actions_count):
        locator = locators.ACTIONS_SHOWN_COUNT

        return int(self.wait_for_text_in_element_to_equal(locator, str(expected_actions_count)))