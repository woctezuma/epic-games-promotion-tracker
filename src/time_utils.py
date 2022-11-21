from datetime import datetime

from src.data_utils import DATA_FOLDER
from src.markdown_utils import MISSING_DATA, TIME_FIELDS


def get_current_date():
    return datetime.now()


def get_folder_name_for_specific_day(date):
    return f"{DATA_FOLDER}/{date.year}/{date.month:02}"


def get_fname_for_specific_day(date):
    folder_name = get_folder_name_for_specific_day(date)
    return f"{folder_name}/{date.day:02}.json"


def get_fname_for_today():
    date = get_current_date()
    return get_fname_for_specific_day(date)


def format_dates_for_display(data):
    for entry in data:
        format_dates_in_dict(entry)

    return data


def format_dates_in_dict(entry):
    for k in TIME_FIELDS:
        entry[k] = prepare_date_for_display(entry[k])


def prepare_date_for_display(date_str: str | None) -> str:
    if date_str is None or date_str == MISSING_DATA:
        output = MISSING_DATA
    else:
        s = date_str.replace('T', ' ')
        output = f"{s[:13]}h"
    return output
