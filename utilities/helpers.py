from datetime import datetime
from random import choice


def get_random_number():
    return choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def get_date():
    date = datetime.now()

    return f'{date.month}/{date.day}/{date.year}'


def get_timestamp():
    date = datetime.now()

    return f'{date.hour}:{date.minute}:{date.second}'