import logging

from . import locators
from pages.base_page import BasePage


class DeleteActionModal(BasePage):
    def click_cancel_button(self):
        logging.info("Click the 'Cancel' button.")
        self.find_clickable_element(locators.CANCEL_BUTTON).click()

    def click_ok_button(self):
        logging.info("Click the 'Ok' button.")
        self.find_clickable_element(locators.OK_BUTTON).click()