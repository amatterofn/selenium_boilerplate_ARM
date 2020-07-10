from selenium.webdriver.common.by import By

OK_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.modal-footer .btn-success'
}

CANCEL_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.modal-footer .btn-default'
}

CONFIRM_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.modal-dialog--inner .modal-footer .btn-success'
}

MODAL_CONTAINER = {
    'by': By.CLASS_NAME,
    'value': 'modal-dialog--inner'
}

MAIN_MODAL_CONTAINER = {
    'by': By.CLASS_NAME,
    'value': 'modal-header'
}


MODAL_TITLE = {
    'by': By.CSS_SELECTOR,
    'value': '.modal-header .modal-title'
}

MODAL_FADE_IN = {
    'by': By.CSS_SELECTOR,
    'value': '.modal-backdrop.fade.in'
}