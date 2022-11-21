from src.markdown_utils import MISSING_DATA, TITLE_FIELDS


def format_titles_for_display(data):
    for entry in data:
        format_titles_in_dict(entry)

    return data


def format_titles_in_dict(entry):
    for k in TITLE_FIELDS:
        entry[k] = prepare_title_for_display(entry[k])


def prepare_title_for_display(title: str) -> str:
    if title is None:
        output = MISSING_DATA
    else:
        output = remove_spurious_spaces(title)
    return output


def remove_spurious_spaces(title: str) -> str:
    """This removes repeated spaces, as well as leading and trailing spaces.
    Reference: https://stackoverflow.com/a/2077944/376454
    """
    return " ".join(title.split())
