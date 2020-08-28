import logging
import pytest

from random import choice

from api import actions, current_user
from utilities.helpers import get_date, get_timestamp
from utilities.validators import date_is_valid, time_is_valid


@pytest.mark.actions_crud
class TestActionsCRUD:
    @pytest.fixture(autouse=True, scope='session')
    def test_set_up_and_tear_down_session(self, authenticated_driver, auth_header):
        logging.info("Before all test cases run.")

        # run the whole test suite
        yield

        logging.info("After all test cases run.")

    @pytest.fixture(autouse=True)
    def test_set_up_and_tear_down_test_function(self, actions_page, auth_header):
        logging.info("Before each test case runs.")
        actions.delete_all_actions(auth_header)
        actions_page.navigate()

        # run an individual test case
        yield

        logging.info("After each test case runs.")

    def test_action_counts_for_empty_state(self, actions_page):
        logging.info("Verify that the 'Total Actions' count equals 0.")
        assert actions_page.total_actions_count == 0

        logging.info("Verify that the 'Actions this Week' count equals 0.")
        assert actions_page.actions_this_week_count == 0

        logging.info("Verify that the 'Actions this Month' count equals 0.")
        assert actions_page.actions_this_month_count == 0

        no_actions_message = "No actions yet."
        create_action_message = (
            "Create one to record meetings, calls, and other actions to share past and future activity with your team."
        )
        logging.info("Verify that the correct help text appears on the screen.")
        assert no_actions_message in actions_page.empty_state_help_text
        assert create_action_message in actions_page.empty_state_help_text

        logging.info("Verify that the empty state 'Add Action' button is displayed.")
        assert actions_page.empty_state_add_action_button.is_displayed()

    def test_user_sees_correct_default_state_for_action_modal(self, action_modal, actions_page, auth_header):
        actions_page.click_empty_state_add_action_button()

        logging.info("Verify that the action modal is displayed.")
        assert action_modal.is_displayed

        logging.info("Verify that that the action modal has the header 'Add Action.'")
        assert action_modal.modal_header_text == "Add Action"

        logging.info("Verify that the 'Start Date' in the action modal is valid.")
        assert date_is_valid(action_modal.start_date_value)

        logging.info("Verify that the 'Start Time' in the action modal is valid.")
        assert time_is_valid(action_modal.start_time_value)

        logging.info("Verify that the 'End Date' in the action modal is valid.")
        assert date_is_valid(action_modal.end_date_value)

        logging.info("Verify that the 'End Time' in the action modal is valid.")
        assert time_is_valid(action_modal.end_time_value)

        logging.info("Verify that the 'Action Type' is 'Meeting.'")
        assert action_modal.selected_action_type == "Meeting"

        user = current_user.get_current_user(auth_header)
        user_full_name = f"{user['first_name']} {user['last_name']}"

        logging.info(f"Verify that '{user_full_name}' is added as an attendee.")
        assert action_modal.added_attendees == [user_full_name]

        logging.info("Verify that there are no linked items.")
        assert action_modal.added_linked_items == []

        logging.info("Verify that there are no added labels.")
        assert action_modal.added_labels == []

        logging.info("Verify that there are no added issues.")
        assert action_modal.added_issues == []

        logging.info("Verify that there is no summary.")
        assert action_modal.current_summary_text == ''

    def test_user_can_open_actions_modal_with_empty_state_add_action_button_and_close_it_with_cancel_button(
        self,
        action_modal,
        actions_page,
        confirmation_modal
    ):
        actions_page.click_empty_state_add_action_button()
        action_modal.click_cancel_button()
        confirmation_modal.click_cancel_button()

        logging.info("Verify that the action modal is visible.")
        assert action_modal.is_displayed

        action_modal.click_cancel_button()
        confirmation_modal.click_confirm_button()

        logging.info("Verify that the action modal is not visible.")
        assert action_modal.is_not_displayed

    def test_user_can_open_actions_modal_with_main_add_action_button_and_close_it_with_x_icon(
        self,
        action_modal,
        actions_page,
        confirmation_modal
    ):
        actions_page.click_add_action_button()

        logging.info('Verifying Action Modal is visible.')
        assert action_modal.is_displayed

        action_modal.click_close_icon()
        confirmation_modal.click_cancel_button()

        logging.info('Verifying Action Modal is still visible.')
        assert action_modal.is_displayed

        action_modal.click_close_icon()
        confirmation_modal.click_confirm_button()

        logging.info('Verifying Action Modal is no longer visible.')
        assert action_modal.is_not_displayed

    @pytest.mark.debug
    def test_user_can_create_a_new_action(self, action_modal, actions_page, auth_header):
        actions_page.click_add_action_button()

        action_modal.enter_start_date('8/14/2019')
        action_modal.enter_start_time('6:00am')
        action_modal.enter_end_date('8/14/2019')
        action_modal.enter_end_time('5:00pm')
        action_modal.set_action_type('Phone Call')
        action_modal.add_linked_item('US HR 1478', 'US - HR 1478')
        action_modal.add_labels(('agriculture', 'farming', 'welfare'))
        action_modal.add_issue('Agriculture')

        action_summary_text = f'{get_date()} {get_timestamp()} - This is my summary text.'
        action_modal.add_summary(action_summary_text)

        action_modal.click_save_button()

        expected_action_1_start = "Aug 14, 2019 6:00 AM"
        logging.info(f'Verifying that the "Start" value for the action in position 1 equals "{expected_action_1_start}"')
        assert actions_page.get_action_start_by_position(1) == expected_action_1_start

        expected_action_1_end = "Aug 14, 2019 5:00 PM"
        logging.info(f'Verifying that the "End" value for the action in position 1 equals "{expected_action_1_end}"')
        assert actions_page.get_action_end_by_position(1) == expected_action_1_end

        user = current_user.get_current_user(auth_header)
        user_full_name = f"{user['first_name']} {user['last_name']}"

        expected_creator = user_full_name
        logging.info(f'Verifying that the "Creator" value for the action in position 1 equals "{expected_creator}"')
        assert actions_page.get_action_creator_by_position(1) == expected_creator

        expected_attendees = [user_full_name]
        logging.info(f'Verifying that the "Attendees" value for the action in position 1 equals "{expected_attendees}"')
        assert actions_page.get_action_attendees_by_position(1) == expected_attendees

        expected_issues = ['Agriculture']
        logging.info(f'Verifying that the "Issues" value for the action in position 1 equals "{expected_issues}"')
        assert actions_page.get_action_issues_by_position(1) == expected_issues

        logging.info(f'Verifying that the "Summary" value for the action in position 1 equals "{action_summary_text}"')
        assert actions_page.get_action_summary_by_position(1) == action_summary_text

    def test_user_can_delete_action(self, actions_page, confirmation_modal, auth_header):
        actions.create_action(auth_header, summary='This action needs to be deleted.')

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

    def test_user_can_batch_delete_actions(self, actions_page, auth_header, delete_action_modal):
        for number in range(1, 11):
            actions.create_action(auth_header, summary=f'Action #{number}')

        actions_page.navigate()

        expected_actions_count = 10
        logging.info(f'Verifying that {expected_actions_count} actions are visible.')
        assert actions_page.visible_actions_count == expected_actions_count

        actions_page.select_all_actions_on_current_page()

        logging.info('Verifying that 10 actions are selected.')
        assert actions_page.selected_count == '10 Selected'

        actions_page.click_delete_button()
        delete_action_modal.click_cancel_button()

        actions_page.click_delete_button()
        delete_action_modal.click_ok_button()

        expected_actions_count = 0
        actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
        logging.info(f'Verify that the "Total Actions" count equals {expected_actions_count}.')
        assert expected_actions_count == actual_actions_count

        logging.info(f'Verifying that {expected_actions_count} actions are visible.')
        assert actions_page.visible_actions_count == expected_actions_count

        actions_page.navigate()

        actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
        logging.info(f'Verify that the "Total Actions" count equals {expected_actions_count}.')
        assert expected_actions_count == actual_actions_count

        logging.info(f'Verifying that {expected_actions_count} actions are visible.')
        assert actions_page.visible_actions_count == expected_actions_count

    def test_user_can_batch_delete_individual_actions(self, actions_page, auth_header, delete_action_modal):
        for number in range(10, 0, -1):
            actions.create_action(auth_header, summary=f'Action #{number}')

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
        delete_action_modal.click_ok_button()

        expected_actions_count = 7
        actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
        logging.info(f'Verify that the "Total Actions" count equals {expected_actions_count}.')
        assert expected_actions_count == actual_actions_count

        logging.info(f'Verifying that {expected_actions_count} actions are visible.')
        assert actions_page.visible_actions_count == expected_actions_count

        expected_action_summaries = [f'Action #{position}' for position in positions]
        logging.info(f'Verifying that the following actions are visible: {expected_action_summaries}')
        assert actions_page.visible_action_summaries == expected_action_summaries

        actions_page.navigate()

        actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
        logging.info(f'Verify that the "Total Actions" count equals {expected_actions_count}.')
        assert expected_actions_count == actual_actions_count

        logging.info(f'Verifying that {expected_actions_count} actions are visible.')
        assert actions_page.visible_actions_count == expected_actions_count

        logging.info(f'Verifying that the following actions are visible: {expected_action_summaries}')
        assert actions_page.visible_action_summaries == expected_action_summaries

    def test_user_can_search_for_actions_by_action_summary(self, actions_page, auth_header, top_search):
        action_summaries = [
            'this action summary is unique',
            'this action summary is the same',
            'this action summary is the same'
        ]

        for action_summary in action_summaries:
            actions.create_action(auth_header, summary=action_summary)

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

    def test_user_can_load_more_actions(self, actions_page, auth_header):
        logging.info('Creating 40 actions.')
        for number in range(1, 41):
            actions.create_action(auth_header, summary=f'Summary #{number}')

        actions_page.navigate()

        expected_actions_count = 15
        actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
        logging.info(f'Verify that {expected_actions_count} actions are visible.')
        assert actual_actions_count == expected_actions_count

        actions_page.load_more_actions()

        expected_actions_count = 30
        actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
        logging.info(f'Verify that {expected_actions_count} actions are visible.')
        assert actual_actions_count == expected_actions_count

        actions_page.load_more_actions()

        expected_actions_count = 40
        actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
        logging.info(f'Verify that {expected_actions_count} actions are visible.')
        assert actual_actions_count == expected_actions_count