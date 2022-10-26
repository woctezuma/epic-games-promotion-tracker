from src.filter_utils import filter_in_free_games
from src.markdown_utils import format_data_as_markdown
from src.time_utils import formate_dates_for_display

OUTPUT_FOLDER = 'docs'
FREE_GAME_FNAME = f"{OUTPUT_FOLDER}/by_free_game.md"


def write_lines_to_disk(lines, fname):
    with open(fname, 'w', encoding='utf8') as f:
        for line in lines:
            f.write(f"{line}\n")
    return


def write_data_to_disk(data, fname):
    lines = format_data_as_markdown(data)
    write_lines_to_disk(lines, fname)
    return


def write_markdown_files(data):
    data = formate_dates_for_display(data)

    sorted_data = sorted(filter_in_free_games(data), key=lambda x: (x["startDate"], x["title"]))
    write_data_to_disk(sorted_data, f"{FREE_GAME_FNAME}")

    sorted_data = sorted(data, key=lambda x: (x["slug"], x["startDate"]))
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_game_slug.md")

    sorted_data = sorted(data, key=lambda x: (x["title"], x["startDate"]))
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_game_name.md")

    sorted_data = sorted(data, key=lambda x: (x["startDate"], x["title"]))
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_start_date.md")

    sorted_data = sorted(data, key=lambda x: (x["endDate"], x["title"]))
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_end_date.md")

    sorted_data = sorted(data, key=lambda x: (-x["discountPercentage"], x["title"], x["startDate"]))
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_discount_percentage.md")

    return
