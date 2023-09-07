import string
from datetime import datetime


def generate_name():
        datetime_today = datetime.today()
        return f'test-{datetime_today.strftime("%d.%m-%H-%M-%S")}'