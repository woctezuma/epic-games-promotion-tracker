from src.markdown_utils import MISSING_DATA, TIME_FIELDS


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
        s = date_str.replace("T", " ")
        output = f"{s[:13]}h"
    return output
