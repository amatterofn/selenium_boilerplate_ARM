import logging

from . import locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def click_click_here_to_log_in_button(self):
        logging.info('Clicking the "Log In" button.')
        click_here_to_log_in_button = self.find_visible_element(locators.CLICK_HERE_TO_LOG_IN_BUTTON)
        click_here_to_log_in_button.click()

    def click_login_button(self):
        logging.info('Clicking the "Log In" button.')
        login_button = self.find_visible_element(locators.LOGIN_BUTTON)
        login_button.click()

    def enter_email(self, email):
        logging.info(f'Entering "{email}" in the "Email" field.')
        email_input = self.find_visible_element(locators.EMAIL_INPUT)
        email_input.send_keys(email)

    def enter_password(self, password):
        logging.info('Entering password in the "Password" field.')
        password_input = self.find_visible_element(locators.PASSWORD_INPUT)
        password_input.send_keys(password)

    def navigate(self):
        login_page_url = 'https://staging.fiscalnote.com/?error=notauthorized'
        logging.info(f'Navigating to {login_page_url}')
        self.driver.get(login_page_url)

    def login(self, email, password):
        self.navigate()
        self.click_click_here_to_log_in_button()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()