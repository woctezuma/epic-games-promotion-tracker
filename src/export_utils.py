from src.filter_utils import filter_in_free_games
from src.markdown_utils import format_data_as_markdown

OUTPUT_FOLDER = 'docs'


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
    sorted_data = sorted(filter_in_free_games(data), key=lambda x: x["title"])
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_free_game.md")

    sorted_data = sorted(data, key=lambda x: x["slug"])
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_game_slug.md")

    sorted_data = sorted(data, key=lambda x: x["title"])
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_game_name.md")

    sorted_data = sorted(data, key=lambda x: x["startDate"])
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_start_date.md")

    sorted_data = sorted(data, key=lambda x: x["endDate"])
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_end_date.md")

    sorted_data = sorted(data, key=lambda x: x["discountPercentage"], reverse=True)
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_discount_percentage.md")

    return
