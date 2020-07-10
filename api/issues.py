import logging
import requests

from . import current_user

ISSUES_ENDPOINT = 'https://staging.fiscalnote.com/api/2.0/projects'


def create_issue(authorization_header, name='', memberType=4, memberId=18288):
    logging.info(f'Creating issue with name: "{name}"')
    create_issue_response = requests.post(
        ISSUES_ENDPOINT,
        headers=authorization_header,
        json={
            "data":
                {"name": name,
                 "memberType": memberType,
                 "memberId": memberId
                 }
        }
    )

    return create_issue_response.json()


def delete_all_issues(authorization_header):
    all_issues = get_all_issues(authorization_header)
    all_issue_ids = [issue['id'] for issue in all_issues]

    for issue_id in all_issue_ids:
        logging.info(f'Attempting to delete issue with ID {issue_id}')
        delete_response = requests.delete(f'{ISSUES_ENDPOINT}/{issue_id}', headers=authorization_header)

        if delete_response.status_code == 200:
            logging.info('Successfully deleted issue.')
            logging.info(delete_response.elapsed)
        else:
            logging.info('Failed to delete issue')


def get_all_issues(authorization_header, per=100):
    get_all_issues_response = requests.get(
        ISSUES_ENDPOINT,
        headers=authorization_header,
        json={"page": 1,
              "per": per,
              "query": None,
              "sorting": 2
              }
    )

    return get_all_issues_response.json()['results']