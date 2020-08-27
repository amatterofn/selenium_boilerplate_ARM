from . import locators
from pages.base_page import BasePage


class ActionSummaryModal(BasePage):
    @property
    def actions_this_month(self):
        return int(self.find_visible_element(locators.actions_count_by_caption('Actions This Month')).text.strip())

    @property
    def actions_this_week(self):
        return int(self.find_visible_element(locators.actions_count_by_caption('Actions This Week')).text.strip())

    @property
    def total_actions(self):
        return int(self.find_visible_element(locators.actions_count_by_caption('Total Actions')).text.strip())