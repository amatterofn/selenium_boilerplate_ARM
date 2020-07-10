from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import (
    invisibility_of_element,
    visibility_of_all_elements_located,
    visibility_of_element_located,
    presence_of_element_located,
    presence_of_all_elements_located,
    element_to_be_clickable
)
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

BASE_TIMEOUT = 20


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_clickable_element(self, locator, timeout=BASE_TIMEOUT):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(element_to_be_clickable((locator['by'], locator['value'])))
        except TimeoutException:
            return None

    def find_present_element(self, locator, timeout=BASE_TIMEOUT):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(presence_of_element_located((locator['by'], locator['value'])))
        except TimeoutException:
            return None

    def find_present_elements(self, locator, timeout=BASE_TIMEOUT):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(presence_of_all_elements_located((locator['by'], locator['value'])))
        except TimeoutException:
            return []

    def find_visible_element(self, locator, timeout=BASE_TIMEOUT):
        try:
            wait = WebDriverWait(self.driver, timeout)

            return wait.until(visibility_of_element_located((locator['by'], locator['value'])))
        except TimeoutException:
            return None

    def find_visible_elements(self, locator, timeout=BASE_TIMEOUT):
        try:
            wait = WebDriverWait(self.driver, timeout)

            return wait.until(visibility_of_all_elements_located((locator['by'], locator['value'])))
        except TimeoutException:
            return []

    def is_not_visible(self, locator, timeout=BASE_TIMEOUT):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(invisibility_of_element((locator['by'], locator['value'])))

            return True
        except TimeoutException:
            return False

    def is_visible(self, locator, timeout=BASE_TIMEOUT):
        return self.find_visible_element(locator, timeout=timeout) is not None

    def move_to_element(self, locator):
        element = self.find_present_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def wait_for_number_of_elements_to_be_visible(self, locator, expected_count, timeout=BASE_TIMEOUT):
        # Create a seconds waited variable and set it to 0.
        # Create a number of elements variable and set it to 0.
        #
        # Repeat the following steps for as long as the number of seconds waited is less than the timeout.
        #
        # Calculate the number of visible elements. (The built-in len() function and our find_visible_elements
        # function will be helpful here.)
        #
        # If the number of elements equals the expected count, return the number of elements.
        #
        # Otherwise, sleep for 1 second and increment the seconds waited counter.
        #
        # If the timeout is hit, return the number of elements.
        pass

    def wait_for_text_in_element_to_equal(self, locator, expected_text, timeout=BASE_TIMEOUT):
        element_text = None
        seconds_waited = 0

        while seconds_waited <timeout:
            element_text = self.find_visible_element(locator).text.strip()

            if element_text == expected_text:
                return element_text
            else:
                sleep(1)
                seconds_waited = seconds_waited + 1

        return element_text
