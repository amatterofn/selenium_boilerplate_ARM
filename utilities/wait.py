from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable,
    visibility_of_element_located
)
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_element_to_be_visible(driver, locator, timeout=15):
    try:
        wait = WebDriverWait(driver, timeout)

        return wait.until(visibility_of_element_located((locator['by'], locator['value'])))
    except TimeoutException:
        return None







