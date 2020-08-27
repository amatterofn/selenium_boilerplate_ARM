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

SEE_ACTIONS_SUMMARY_LINK = {
    'by': By.CSS_SELECTOR,
    'value': '.actions-summary-bar button'
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
        'value': f'//td[contains(@class, "actions-row__summary-col")]//p[contains(text(), "{action_summary}")]//ancestor::tr//div[contains(@class, "actions-row__checkbox")]'
    }


def action_checkbox_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'(//tr[contains(@class, "actions-row__info")])[{position}]//div[contains(@class, "actions-row__checkbox")]'
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


def actions_filter_by_filter_text(filter_text):
    return {
        'by': By.XPATH,
        'value': f'//div[contains(@class, "actions-list-header")]//span[contains(text(), "{filter_text}")]//ancestor::span[contains(@class, "fn-popover__trigger")]'
    }


# Needed to add the end_or_start locator to the following three locators since the locator would otherwise find duplicate
# locators for the start/end filters.
def date_by_date_text(end_or_start, desired_date):
    return {
        'by': By.XPATH,
        'value': f'//div[@id="fn-calendar-widget-{end_or_start}"]//div[contains(@class, "pmu-days")]//div[contains(@class, "pmu-button") and not(contains(@class, "pmu-not-in-month")) and text()="{desired_date}"]'
    }


def date_filter_apply_button(end_or_start):
    return {
        'by': By.XPATH,
        'value': f'//div[@id="fn-calendar-widget-{end_or_start}"]//ancestor::div[contains(@class, "popover-content")]//button[contains(text(), "Apply")]'
    }


def date_filter_previous_next(end_or_start, previous_next):
    return {
        'by': By.CSS_SELECTOR,
        'value': f'#fn-calendar-widget-{end_or_start} .pmu-{previous_next}'
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