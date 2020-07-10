import logging

from . import locators
from pages.base_page import BasePage


class TopSearch(BasePage):
    @property
    def search_button(self):
        return self.find_visible_element(locators.SEARCH_BUTTON)

    @property
    def search_input(self):
        return self.find_visible_element(locators.SEARCH_INPUT)

    def perform_search(self, search_query):
        if len(self.search_input.get_attribute('value')) > 0:
            logging.info('Clearing search input.')
            self.search_input.clear()

        logging.info(f'Entering search query of "{search_query}"')
        self.search_input.send_keys(search_query)

        logging.info('Clicking "Search" button.')
        self.search_button.click()