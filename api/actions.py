import logging
import requests

from datetime import datetime, timedelta

from . import current_user

ACTIONS_ENDPOINT = 'https://staging.fiscalnote.com/api/2.0/actions'

ACTION_TYPE_MAPPING = {
    'Meeting': 3,
    'Roundtable': 14
}


def create_action(
    authorization_header,
    action_type='Meeting',
    attendees=None,
    end_date=datetime.now() + timedelta(hours=1),
    start_date=datetime.now(),
    summary=''
):
    if not attendees:
        attendees = [current_user.get_current_user(authorization_header)['id']]

    logging.info(f'Creating action with summary: "{summary}"')
    create_action_response = requests.post(
        ACTIONS_ENDPOINT,
        headers=authorization_header,
        json={
            "summary": summary,
            "attendees": attendees,
            "linkedItems": [],
            "actionType": ACTION_TYPE_MAPPING.get(action_type),
            "hashtags": [],
            "startDate": start_date.isoformat(),
            "endDate": end_date.isoformat(),
            "projects": [],
            "labels": []
        }
    )

    return create_action_response.json()


def delete_all_actions(authorization_header):
    all_actions = get_all_actions(authorization_header)
    all_action_ids = [action['id'] for action in all_actions]

    for action_id in all_action_ids:
        logging.info(f'Attempting to delete action with ID {action_id}')
        delete_response = requests.delete(f'{ACTIONS_ENDPOINT}/{action_id}', headers=authorization_header)

        if delete_response.status_code == 200:
            logging.info('Successfully deleted action.')
            logging.info(delete_response.elapsed)
        else:
            logging.info('Failed to delete action.')


def get_all_actions(authorization_header, page=1, per=100):
    get_all_actions_response = requests.post(
        f'{ACTIONS_ENDPOINT}/search',
        headers=authorization_header,
        json={
            "query": "",
            "fromDate": None,
            "toDate": None,
            "actionTypes": [],
            "createdByUserIds": [],
            "attendees": [],
            "scraperBillIds": [],
            "billStates": [],
            "scraperLegislatorIds": [],
            "legislatorStates": [],
            "legislatorParties": [],
            "legislatorChambers": [],
            "scraperCommitteeIds": [],
            "personContactIds": [],
            "organizationContactIds": [],
            "fedRegDocketIds": [],
            "fedRegDocumentIds": [],
            "utilRegDocketIds": [],
            "utilRegDocketStates": [],
            "scraperAgencyIds": [],
            "stateRegulationIds": [],
            "stateRegulationStates": [],
            "chinaRegulationIds": [],
            "intlBillIds": [],
            "hashtags": [],
            "withoutAssociatedItems": False,
            "id": None,
            "projectIds": [],
            "page": page,
            "per": per,
            "entityParams": {
                "billParams": {
                    "ids": [],
                    "states": []
                },
                "personContactParams": {
                    "ids": []
                },
                "orgContactParams": {
                    "ids": []
                },
                "legislatorParams": {
                    "ids": [],
                    "states": [],
                    "parties": [],
                    "chambers": []
                },
                "fedRegDocketParams": {
                    "ids": [],
                    "agencyIds": []
                },
                "fedRegDocumentParams": {
                    "ids": [],
                    "agencyIds": []
                },
                "committeeParams": {
                    "ids": []
                },
                "utilityRegDocketParams": {
                    "ids": []
                },
                "stateRegParams": {
                    "ids": [],
                    "states": []
                },
                "chinaRegulationParams": {
                    "ids": []
                }
            }
        }
    )

    return get_all_actions_response.json()['results']