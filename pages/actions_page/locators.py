from selenium.webdriver.common.by import By

ACTION_CONTAINER = {
    'by': By.CLASS_NAME,
    'value': 'actions-row__info'
}

ACTION_SUMMARY = {
    'by': By.CSS_SELECTOR,
    'value': '.actions-row__info .actions-row__summary-col'
}

ACTIONS_SHOWN_COUNT = {
    'by': By.CSS_SELECTOR,
    'value': '.results-count-container .results-count'
}

ADD_ACTION_BUTTON = {
    'by': By.XPATH,
    'value': '//button[text()="+ Add"]'
}

DELETE_BUTTON = {
    'by': By.XPATH,
    'value': '//span[contains(text(), "Delete")]//ancestor::button'
}

SEE_ACTIONS_SUMMARY_LINK = {
    'by': By.XPATH,
    'value': '//button[contains(string(),"See Actions Summary")]'
}

START_DATE_FILTER_BUTTON = {
    'by': By.XPATH,
    'value': '//span[contains(text(),"Start")]'
}

EMPTY_STATE_ADD_ACTION_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.actions-search__empty-content button'
}

EMPTY_STATE_HELP_TEXT = {
    'by': By.CSS_SELECTOR,
    'value': '.actions-search__empty-content h5'
}

LOAD_MORE = {
    'by': By.CLASS_NAME,
    'value': 'actions-search__load-more'
}

ACTION_SUMMARY_TEXT = {
    'by': By.CSS_SELECTOR,
    'value': '.actions-row_summary-col'
}

SELECT_DROPDOWN = {
    'by': By.CLASS_NAME,
    'value': 'content-table__select-all'
}

SELECTED_COUNT = {
    'by': By.CLASS_NAME,
    'value': 'actions-search__selected-text'
}


def action_attendees_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'(//tr[contains(@class, "actions-row__info")])[{position}]//td[contains(@class, "actions-row__attendees-col")]//div[contains(@class, "trunk8-original")]'
    }


def action_checkbox_by_action_summary(action_summary):
    return {
        'by': By.XPATH,
        'value': f'//td[contains(@class,"actions-row__summary-col")]//p[contains(text(), "{action_summary}")]//ancestor::tr//div[contains(@class,"actions-row__checkbox")]'
    }


def action_checkbox_by_position(position):
    return{
        'by': By.XPATH,
        'value': f'(//tr[contains(@class,"actions-row__info")])[{position}]//div[contains(@class,"actions-row__checkbox")]'
    }


def action_count_by_description(description):
    return {
        'by': By.XPATH,
        'value': f'//figcaption[contains(string(), "{description}")]//preceding-sibling::figure'
    }


def action_creator_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'(//tr[contains(@class, "actions-row__info")])[{position}]//td[contains(@class, "actions-row__creator-col")]//div[contains(@class, "trunk8-original")]'
    }


def action_end_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'//tr[contains(@class, "actions-row__info")][{position}]//td[contains(@class, "actions-row__date-col")][2]'
    }


def action_issues_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'(//tr[contains(@class, "actions-row__info")])[{position}]//td[contains(@class, "actions-row__projects-col")]//div[contains(@class, "trunk8-original")]//span'
    }


def action_start_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'//tr[contains(@class, "actions-row__info")][{position}]//td[contains(@class, "actions-row__date-col")][1]'
    }


def action_summary_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'(//tr[contains(@class, "actions-row__info")])[{position}]//td[contains(@class, "actions-row__summary-col")]//div[contains(@class, "trunk8-original")]'
    }


def delete_action_icon_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'(//i[contains(@class, "ion-trash-b")])[{position}]'
    }


def select_dropdown_option_by_option_text(option_text):
    return {
        'by': By.XPATH,
        'value': f'//span[contains(@class, "content-table__select-all")]//li//a[contains(text(), "{option_text}")]'
    }





def action_linked_items_by_position(position):
    return{
        'by': By.XPATH,
        'value': f'//tr[contains(@class, "actions-row__info")][{position}]//td[contains(@class, "actions-row__associated-items")]//div[contains(@class, "trunk8-original")]//span[contains(@class, "actions-pane__item-badge")]'
    }

def action_edit_button_by_position(position):
    return{
        'by': By.XPATH,
        'value': f'//tr[contains(@class, "actions-row__info")][{position}]//td[contains(@class, "actions-row__modify")]//i[contains(@class, "ion-edit")]'
    }