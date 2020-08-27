import logging
import pytest

from datetime import datetime
from time import sleep

from api import actions


@pytest.mark.actions_filters
class TestActionSummaryModalAndStartAndEndDateFilters:
    @pytest.fixture(autouse=True, scope='session')
    def test_set_up_and_tear_down_session(self, authenticated_driver, auth_header):
        actions.delete_all_actions(auth_header)

        now = datetime.now()

        if now.month == 1:
            # Set the start/end date to December 15th of previous year.
            past_action_end_date = datetime(now.year - 1, 12, 15, 13, 0, 0)
            past_action_start_date = datetime(now.year - 1, 12, 15, 12, 0, 0)
        else:
            # Set the start/end date to 15th of previous month in the current year
            past_action_end_date = datetime(now.year, now.month - 1, 15, 13, 0, 0)
            past_action_start_date = datetime(now.year, now.month - 1, 15, 12, 0, 0)

        logging.info('Creating 5 past actions.')
        for number in range(5):
            actions.create_action(
                auth_header,
                end_date=past_action_end_date,
                start_date=past_action_start_date,
                summary='past action'
            )

        logging.info('Creating 10 actions on current day.')
        for number in range(10):
            actions.create_action(auth_header, summary='current date')

        if now.month == 12:
            # Set the start/end date to January 15th of next year
            future_action_end_date = datetime(now.year + 1, 1, 15, 13, 0, 0)
            future_action_start_date = datetime(now.year + 1, 1, 15, 12, 0, 0)
        else:
            # Set the start/end date to 15th of next month in current year
            future_action_end_date = datetime(now.year, now.month + 1, 15, 13, 0, 0)
            future_action_start_date = datetime(now.year, now.month + 1, 15, 12, 0, 0)

        logging.info('Creating 5 future actions.')
        for number in range(5):
            actions.create_action(
                auth_header,
                end_date=future_action_end_date,
                start_date=future_action_start_date,
                summary='future action'
            )

    @pytest.fixture(autouse=True)
    def set_up_and_tear_down_test_case(self, actions_page):
        actions_page.navigate()

        expected_actions_count = 15
        actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
        logging.info(f'Verify that {expected_actions_count} actions are visible.')
        assert actual_actions_count == expected_actions_count

    def test_user_can_open_actions_summary_modal(self, actions_page, actions_summary_modal):
        actions_page.click_see_actions_summary_link()

        expected_total_actions_count = 20
        logging.info(f'Verify that "Total Actions" equals {expected_total_actions_count}')
        assert actions_summary_modal.total_actions == expected_total_actions_count

        logging.info(f'Verify that "Total Actions" in the modal matches what is on the page.')
        assert actions_summary_modal.total_actions == actions_page.total_actions_count

        expected_actions_this_month = 10
        logging.info(f'Verify that "Actions This Month" equals {expected_actions_this_month}')
        assert actions_summary_modal.actions_this_month == expected_actions_this_month

        logging.info(f'Verify that "Actions This Month" in the modal matches what is on the page.')
        assert actions_summary_modal.actions_this_month == actions_page.actions_this_month_count

        expected_actions_this_week = 10
        logging.info(f'Verify that "Actions This Week" equals {expected_actions_this_week}')
        assert actions_summary_modal.actions_this_week == expected_actions_this_week

        logging.info(f'Verify that "Actions This Week" in the modal matches what is on the page.')
        assert actions_summary_modal.actions_this_week == actions_page.actions_this_week_count

    def test_user_can_filter_by_start_and_end_date_to_find_past_actions(self, actions_page):
        actions_page.open_filter_by_filter_text("Start")
        actions_page.move_calendar_widget_back('start')
        actions_page.click_date('start', 8)
        actions_page.click_date_filter_apply_button('start')

        actions_page.open_filter_by_filter_text("End")
        actions_page.move_calendar_widget_back('end')
        actions_page.click_date('end', 22) # TODO: This line of code is occasionally flaky. Please fix.
        actions_page.click_date_filter_apply_button('end')

        expected_actions_count = 5
        actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
        logging.info(f'Verify that {expected_actions_count} actions are visible.')
        assert actual_actions_count == expected_actions_count

        expected_action_summaries = ['past action', 'past action', 'past action', 'past action', 'past action']
        logging.info(f'Verify that the following action summaries are visible: {expected_action_summaries}')
        assert actions_page.visible_action_summaries == expected_action_summaries

    def test_user_can_filter_by_start_and_end_date_to_find_actions_from_today(self, actions_page):
        current_day = datetime.now().day

        actions_page.open_filter_by_filter_text("Start")
        actions_page.click_date('start', current_day)
        actions_page.click_date_filter_apply_button('start')

        sleep(2) # Todo: Remove this sleep.
        actions_page.open_filter_by_filter_text("End")
        actions_page.click_date('end', current_day) # TODO: This line of code is occasionally flaky. Please fix.
        actions_page.click_date_filter_apply_button('end')

        expected_actions_count = 10
        actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
        logging.info(f'Verify that {expected_actions_count} actions are visible.')
        assert actual_actions_count == expected_actions_count

        expected_action_summaries = ['current date'] * 10
        logging.info(f'Verify that the following action summaries are visible: {expected_action_summaries}')
        assert actions_page.visible_action_summaries == expected_action_summaries

    def test_user_can_filter_by_start_and_end_date_to_find_future_actions(self, actions_page):
        actions_page.open_filter_by_filter_text("Start")
        actions_page.move_calendar_widget_forward('start')
        actions_page.click_date('start', 8)
        actions_page.click_date_filter_apply_button('start')

        actions_page.open_filter_by_filter_text("End")
        actions_page.move_calendar_widget_forward('end')
        actions_page.click_date('end', 22) # TODO: This line of code is occasionally flaky. Please fix.
        actions_page.click_date_filter_apply_button('end')

        expected_actions_count = 5
        actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
        logging.info(f'Verify that {expected_actions_count} actions are visible.')
        assert actual_actions_count == expected_actions_count

        sleep(2)  # Todo: Remove this sleep

        expected_action_summaries = ['future action'] * 5
        logging.info(f'Verify that the following action summaries are visible: {expected_action_summaries}')
        assert actions_page.visible_action_summaries == expected_action_summaries