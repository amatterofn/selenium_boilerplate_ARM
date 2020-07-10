import pytest

from time import sleep

USERNAME_FIELD_ID = 'username'
PASSWORD_FIELD_ID = 'password'
LOG_IN_BUTTON_CLASS_NAME = 'fa-sign-in'
FLASH_MESSAGE_ID = 'flash'
LOG_OUT_BUTTON_CLASS_NAME = 'icon-signout'


def test_user_can_log_in(driver):
    driver.get('https://the-internet.herokuapp.com/login')

    username_field = driver.find_element_by_id(USERNAME_FIELD_ID)
    username_field.send_keys('tomsmith')

    password_field = driver.find_element_by_id(PASSWORD_FIELD_ID)
    password_field.send_keys('SuperSecretPassword!')

    log_in_button = driver.find_element_by_class_name(LOG_IN_BUTTON_CLASS_NAME)
    log_in_button.click()

    flash_message = driver.find_element_by_id(FLASH_MESSAGE_ID)
    assert 'You logged into a secure area!' in flash_message.text

    log_out_button = driver.find_element_by_class_name(LOG_OUT_BUTTON_CLASS_NAME)
    log_out_button.click()

    flash_message = driver.find_element_by_id(FLASH_MESSAGE_ID)
    assert 'You logged out of the secure area!' in flash_message.text

    sleep(10)

@pytest.mark.new_login
def test_user_sees_error_message_when_clicking_log_in_button_with_no_credentials(driver):
    driver.get('https://the-internet.herokuapp.com/login')

    log_in_button = driver.find_element_by_class_name(LOG_IN_BUTTON_CLASS_NAME)
    log_in_button.click()

    flash_message = driver.find_element_by_id(FLASH_MESSAGE_ID)
    assert 'Your username is invalid!' in flash_message.text