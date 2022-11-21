from pathlib import Path

from src.data_utils import PROMOTION_DATA_FNAME
from src.download_utils import download_upcoming_promotions
from src.export_utils import write_markdown_files
from src.json_utils import load_json, save_json
from src.utils import unique


def main():
    force_update = True

    if force_update or not Path(PROMOTION_DATA_FNAME).exists():
        print("Updating JSON.")
        data = download_upcoming_promotions()
        data = sorted(data, key=lambda x: (x["title"], x["startDate"], -x["discountPercentage"]))
        save_json(data, PROMOTION_DATA_FNAME, prettify=True)
    else:
        data = load_json(PROMOTION_DATA_FNAME)

    print("Updating Markown.")
    data = unique(data)
    write_markdown_files(data)


if __name__ == "__main__":
    main()
