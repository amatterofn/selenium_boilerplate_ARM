from . import locators
from pages.base_page import BasePage


class StateLegislatorsPage(BasePage):
    @property
    def legislators_name(self):
        return self.find_visible_element(locators.LEGISLATORS_NAME).text

    def navigate(self):
        self.driver.get('https://staging.fiscalnote.com/legislators/10002298')
