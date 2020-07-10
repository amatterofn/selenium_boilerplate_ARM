from . import locators
from pages.base_page import BasePage


class HomePage(BasePage):
    @property
    def welcome_message(self):
        return self.find_visible_element(locators.WELCOME_MESSAGE).text
