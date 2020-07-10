from selenium.webdriver.common.by import By


CLICK_HERE_TO_LOG_IN_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.sign-in-form button'
}

EMAIL_INPUT = {
    'by': By.NAME,
    'value': 'email'
}

PASSWORD_INPUT = {
    'by': By.NAME,
    'value': 'password'
}

LOGIN_BUTTON = {
    'by': By.CLASS_NAME,
    'value': 'auth0-lock-submit'
}