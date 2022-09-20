from src.parse_store_data import get_total_num_store_elements, get_store_elements
from src.parse_store_element import to_upcoming_promotion
from src.query_store_data import to_store_data

MAX_STEP_SIZE = 1000


def download_upcoming_promotions():
    dummy_store_data = to_store_data(cursor=0, step=1)
    num_elements = get_total_num_store_elements(dummy_store_data)

    all_upcoming_promotions = []

    for cursor in range(0, num_elements, MAX_STEP_SIZE):
        print(f'Cursor = {cursor}')
        store_data = to_store_data(cursor=cursor, step=MAX_STEP_SIZE)
        store_elements = get_store_elements(store_data)

        promos = [to_upcoming_promotion(e) for e in store_elements]
        all_upcoming_promotions += [p for p in promos if p is not None]

    return all_upcoming_promotions
