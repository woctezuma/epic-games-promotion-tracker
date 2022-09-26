from pathlib import Path

from src.download_utils import download_upcoming_promotions
from src.export_utils import write_markdown_files
from src.json_utils import save_json, load_json
from src.time_utils import get_fname_for_today


def main():
    output_fname = get_fname_for_today()
    Path(output_fname).parent.mkdir(parents=True, exist_ok=True)

    requires_to_download_json = not Path(output_fname).exists()
    requires_to_update_markdown = requires_to_download_json

    if requires_to_download_json:
        print('Updating JSON.')
        data = download_upcoming_promotions()
        data = sorted(data, key=lambda x: (x["title"], x["startDate"]))
        save_json(data, output_fname, prettify=True)
    else:
        data = load_json(output_fname)

    if requires_to_update_markdown:
        print('Updating Markown.')
        write_markdown_files(data)

    return


if __name__ == '__main__':
    main()
