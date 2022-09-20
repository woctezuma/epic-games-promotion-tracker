from src.api import send_post_request_to_api


def get_params_to_query_store_data(cursor, step):
    query_str = "{Catalog {searchStore" + f'(start: {cursor}, count: {step}, country: "FR")' + " {elements {"
    meta_data_str = "title catalogNs {mappings {pageSlug}} promotions {upcomingPromotionalOffers {"
    promotion_str = "promotionalOffers {startDate endDate discountSetting {discountPercentage} }"
    paging_str = "}}} paging {count total} }}}"

    params = {"query": query_str + meta_data_str + promotion_str + paging_str}

    return params


def to_store_data(cursor, step, verbose=True):
    params = get_params_to_query_store_data(cursor, step)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        store_data = data["data"]["Catalog"]["searchStore"]
    except (TypeError, KeyError) as e:
        store_data = None
    return store_data
