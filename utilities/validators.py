from datetime import datetime


def date_is_valid(date, date_format="%m/%d/%Y"):
    try:
        datetime.strptime(date, date_format)

        return True
    except ValueError:
        raise Exception(f'{date} does not match the expected date format {date_format}.')


def time_is_valid(time, time_format="%I:%M%p"):
    try:
        datetime.strptime(time, time_format)

        return True
    except ValueError:
        raise Exception(f'{time} does not not match the expected time format {time_format}')