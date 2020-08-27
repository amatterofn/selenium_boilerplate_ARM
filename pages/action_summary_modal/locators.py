from selenium.webdriver.common.by import By


def actions_count_by_caption(caption):
    return {
        'by': By.XPATH,
        'value': f'//div[contains(@class, "modal-body")]//figcaption[contains(string(), "{caption}")]//preceding-sibling::figure'
    }