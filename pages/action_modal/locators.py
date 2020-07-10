from selenium.webdriver.common.by import By

ATTENDEE = {
    'by': By.XPATH,
    'value': '//label[text()="Attendees"]//following-sibling::div[@class="actions-modal__selectize-container"]//div[@class="option"]'
}

CANCEL_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.actions-modal__footer .btn-default'
}

DELETE_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.actions-modal__footer .btn-danger'
}

CLOSE_ICON = {
    'by': By.CSS_SELECTOR,
    'value': '.modal-header .close'
}

ISSUE = {
    'by': By.CSS_SELECTOR,
    'value': '.project-selection__container .project__bubble p'
}

ISSUE_INPUT = {
    'by': By.CSS_SELECTOR,
    'value': '.project-selection__wrapper input'
}

LABEL = {
    'by': By.CSS_SELECTOR,
    'value': '.label-selection__container .label__bubble p'
}

LABEL_INPUT = {
    'by': By.CSS_SELECTOR,
    'value': '.label-selection__wrapper input'
}

LINKED_ITEM = {
    'by': By.CSS_SELECTOR,
    'value': '.search-input-container .selectize-input .option'
}

LINKED_ITEM_INPUT = {
    'by': By.ID,
    'value': 'linked-items-selectize-selectized'
}

ATTENDEE_INPUT = {
    'by': By.ID,
    'value': 'actions-modal__attendees-selectized'
}

MODAL_HEADER = {
    'by': By.CLASS_NAME,
    'value': 'modal-title'
}

SAVE_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.actions-modal__footer button[type="submit"]'
}

SELECT_ACTION_TYPE = {
    'by': By.CSS_SELECTOR,
    'value': 'select.action-type'
}

START_DATE = {
    'by': By.XPATH,
    'value': '//input[@id="create-action-modal-start-date" or @id="edit-action-start-date"]'
}

START_TIME = {
    'by': By.XPATH,
    'value': '//input[@id="create-action-modal-start-time" or @id="edit-action-start-time"]'
}

END_DATE = {
    'by': By.XPATH,
    'value': '//input[@id="create-action-modal-end-date" or @id="edit-action-end-date"]'
}

END_TIME = {
    'by': By.XPATH,
    'value': '//input[@id="create-action-modal-end-time" or @id="edit-action-end-time"]'
}

SUMMARY_SECTION = {
    'by': By.CSS_SELECTOR,
    'value': '.summary'
}

ADDED_ATTENDEE_INPUT = {
    'by': By.ID,
    'value': 'attendees-selectize-selectized'
}


def issue_by_issue_text(issue_text):
    return {
        'by': By.XPATH,
        'value': f'//div[contains(@class, "project-selection__wrapper")]//li//a[contains(string(), "{issue_text}")]'
    }


def label_by_label_text(label_text):
    return {
        'by': By.XPATH,
        'value': f'//div[@class="label-selection__wrapper"]//li//a[contains(string(), "{label_text}")]'
    }


def linked_item_by_linked_item_text(linked_item_text):
    return {
        'by': By.XPATH,
        'value': f'//div[contains(@class, "option") and contains(string(), "{linked_item_text}")]'
    }


def attendee_by_attendee_text(attendee_text):
    return {
        'by': By.XPATH,
        'value': f'//div[contains(@class, "option") and contains(string(), "{attendee_text}")]'
    }