from selenium.webdriver.common.by import By

MODAL_HEADER = {
    'by': By.CLASS_NAME,
    'value': 'modal-title'
}


def action_count_by_description(description):
    return {
        'by': By.XPATH,
        'value': f'//div[contains(@class, "modal-body")]//figcaption[contains(string(), "{description}")]//preceding-sibling::figure'
    }