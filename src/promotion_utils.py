def get_upcoming_promotional_offers(store_element):
    try:
        promotion_list = store_element["promotions"]["upcomingPromotionalOffers"]
    except TypeError:
        promotion_list = []

    if len(promotion_list) > 0:
        promotional_offers = promotion_list[0]["promotionalOffers"]
    else:
        promotional_offers = []

    return promotional_offers


def to_promo_element(slug, title, price, promotional_offer):
    # NB: the field name is confusing: this is the ratio between the discounted price and the base price.
    ratio = promotional_offer["discountSetting"]["discountPercentage"]

    promo_element = {
        "slug": slug,
        "title": title,
        "originalPrice": price,
        "startDate": promotional_offer["startDate"],
        "endDate": promotional_offer["endDate"],
        "discountPercentage": 100 - ratio,
        "isFree": bool(ratio == 0)
    }

    return promo_element
