from src.api import send_post_request_to_api


def get_params_to_query_store_data(cursor, step, include_dlc=False):
    if include_dlc:
        category_str = ""
    else:
        category_str = 'category: "games/edition/base|software/edition/base|editors|bundles/games|freegames/vaulted", '

    query_str = "{Catalog {searchStore"
    query_str += f'({category_str}start: {cursor}, count: {step}, country: "FR") '
    query_str += "{"
    query_str += "paging {count total} elements {"
    query_str += "title offerMappings {pageSlug} productSlug urlSlug promotions {upcomingPromotionalOffers {"
    query_str += "promotionalOffers {startDate endDate discountSetting {discountPercentage} }"
    query_str += "}} "
    query_str += "id lastModifiedDate countriesBlacklist "
    query_str += 'price(country: "FR") {totalPrice {originalPrice} }'
    query_str += "}"
    query_str += "}}}"

    params = {"query": query_str}

    return params


def to_store_data(cursor, step, include_dlc=False, verbose=True):
    params = get_params_to_query_store_data(cursor, step, include_dlc)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        store_data = data["data"]["Catalog"]["searchStore"]
    except (TypeError, KeyError) as e:
        store_data = None
    return store_data
