import logging

from . import locators
from pages.base_page import BasePage


class ConfirmationModal(BasePage):
    @property
    def cancel_button(self):
        return self.find_visible_element(locators.CANCEL_BUTTON)

    @property
    def confirm_button(self):
        return self.find_visible_element(locators.CONFIRM_BUTTON)

    @property
    def ok_button(self):
        return self.find_visible_element(locators.OK_BUTTON)

    @property
    def is_displayed(self):
        return self.is_visible(locators.MODAL_CONTAINER)

    @property
    def is_not_displayed(self):
        return self.is_not_visible(locators.MODAL_CONTAINER)

    @property
    def main_is_displayed(self):
        return self.is_visible(locators.MAIN_MODAL_CONTAINER)

    @property
    def main_is_not_displayed(self):
        return self.is_not_visible(locators.MAIN_MODAL_CONTAINER)

    @property
    def modal_title(self):
        return self.find_visible_element(locators.MODAL_TITLE).text

    def click_cancel_button(self):
        logging.info('Clicking the "Cancel" button on the Confirmation Modal.')
        self.cancel_button.click()

    def click_confirm_button(self):
        logging.info('Clicking the "Confirm" button on the Confirmation Modal.')
        self.confirm_button.click()

    def click_ok_button(self):
        logging.info('Clicking the "OK" button on the Confirmation Modal.')
        self.ok_button.click()