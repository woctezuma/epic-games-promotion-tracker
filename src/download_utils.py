from src.data_utils import STORE_DATA_FNAME
from src.json_utils import save_json
from src.parse_store_data import get_store_elements, get_total_num_store_elements
from src.parse_store_element import extract_upcoming_promos_from_several_elements
from src.query_store_data import to_store_data

MAX_STEP_SIZE = 40


def download_store_elements(include_dlc=False, save_store_data_to_disk=True):
    dummy_store_data = to_store_data(cursor=0, step=1, include_dlc=include_dlc)
    num_elements = get_total_num_store_elements(dummy_store_data)

    all_store_elements = []

    for cursor in range(0, num_elements, MAX_STEP_SIZE):
        print(f"Cursor = {cursor}")
        store_data = to_store_data(cursor=cursor, step=MAX_STEP_SIZE, include_dlc=include_dlc)
        store_elements = get_store_elements(store_data)

        all_store_elements += store_elements

    if save_store_data_to_disk:
        save_json(all_store_elements, STORE_DATA_FNAME, prettify=True)

    return all_store_elements


def download_upcoming_promotions(include_dlc=False, save_store_data_to_disk=True):
    store_elements = download_store_elements(include_dlc, save_store_data_to_disk)
    all_upcoming_promotions = extract_upcoming_promos_from_several_elements(store_elements)
    return all_upcoming_promotions
