from src.time_utils import prepare_date_for_display

HEADERS = ["Game Slug", "Name", "Discount (%)", "Starts", "Ends"]
TIME_FIELDS = ["startDate", "endDate"]
ENTRY_FIELDS = ["slug", "title", "discountPercentage"] + TIME_FIELDS


def to_table_row(row_no, str_elements):
    concatenated_elements = '|'.join(str_elements)
    line = f"|{row_no}|{concatenated_elements}|"
    return line


def get_headers_line():
    place_holder_for_number = '#'
    return to_table_row(place_holder_for_number, HEADERS)


def get_separator_line():
    place_holder = '---'
    num_headers = len(HEADERS)
    return to_table_row(place_holder, [place_holder] * num_headers)


def format_data_as_markdown(data):
    lines = [get_headers_line(), get_separator_line()]

    for i, entry in enumerate(data, start=1):
        for k in TIME_FIELDS:
            entry[k] = prepare_date_for_display(entry[k])

        line = to_table_row(i, [str(entry[k]) for k in ENTRY_FIELDS])

        lines.append(line)

    return lines
