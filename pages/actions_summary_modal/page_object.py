import logging

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from . import locators
from pages.base_page import BasePage


class ActionsSummaryModal(BasePage):
    @property
    def is_not_displayed(self):
        return self.is_not_visible(locators.MODAL_HEADER)

    @property
    def is_displayed(self):
        return self.is_visible(locators.MODAL_HEADER)

    @property
    def modal_header_text(self):
        return self.find_visible_element(locators.MODAL_HEADER).text

    @property
    def total_actions_count(self):
        return int(self.find_visible_element(locators.action_count_by_description('Total Actions')).text.strip())

    @property
    def actions_this_month_count(self):
        return int(self.find_visible_element(locators.action_count_by_description('Actions This Month')).text.strip())

    @property
    def actions_this_week_count(self):
        return int(self.find_visible_element(locators.action_count_by_description('Actions This Week')).text.strip())
