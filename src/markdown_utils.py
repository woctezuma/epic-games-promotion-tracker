HEADERS = ["Game Slug", "Game Name", "Base Price", "Discount (%)", "Starts", "Ends"]
TIME_FIELDS = ["startDate", "endDate"]
TITLE_FIELDS = ["title"]
PRICE_FIELDS = ["originalPrice"]
ENTRY_FIELDS = ["slug"] + TITLE_FIELDS + PRICE_FIELDS + ["discountPercentage"] + TIME_FIELDS
PLACE_HOLDER = "---"
PLACE_HOLDER_FOR_NUMBER = '#'
MISSING_DATA = "N/A"


def to_table_row(row_no, str_elements):
    concatenated_elements = "|".join(str_elements)
    line = f"|{row_no}|{concatenated_elements}|"
    return line


def get_headers_line():
    return to_table_row(PLACE_HOLDER_FOR_NUMBER, HEADERS)


def get_separator_line():
    place_holder = PLACE_HOLDER
    num_headers = len(HEADERS)
    return to_table_row(place_holder, [place_holder] * num_headers)


def format_data_as_markdown(data, number_rows=False):
    lines = [get_headers_line(), get_separator_line()]

    for i, entry in enumerate(data, start=1):
        if number_rows:
            row_index = i
        else:
            row_index = PLACE_HOLDER_FOR_NUMBER
        line = to_table_row(row_index, [str(entry[k]) for k in ENTRY_FIELDS])

        lines.append(line)

    return lines
