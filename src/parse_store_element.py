def get_upcoming_promotional_offers(store_element):
    try:
        promotion_list = store_element["promotions"]["upcomingPromotionalOffers"]
    except TypeError:
        promotion_list = []

    if len(promotion_list) > 0:
        promotional_offers = promotion_list[0]["promotionalOffers"]
        if len(promotion_list) > 1:
            print(promotion_list)  # TODO
    else:
        promotional_offers = None

    return promotional_offers


def to_upcoming_promotion(store_element):
    promotional_offers = get_upcoming_promotional_offers(store_element)

    if promotional_offers is None:
        promo_element = None
    else:
        first_promotional_offer = promotional_offers[0]
        if len(promotional_offers) > 1:
            print(promotional_offers)  # TODO

        # NB: the field name is confusing: this is the ratio between the discounted price and the base price.
        ratio = first_promotional_offer["discountSetting"]["discountPercentage"]

        slug_mappings = store_element["catalogNs"]["mappings"]
        if slug_mappings is not None and len(slug_mappings) > 0:
            slug = slug_mappings[0]["pageSlug"]
            if len(slug_mappings) > 1:
                print(slug_mappings)  # TODO
        else:
            slug = ""

        promo_element = {
            "slug": slug,
            "title": store_element["title"],
            "startDate": first_promotional_offer["startDate"],
            "endDate": first_promotional_offer["endDate"],
            "discountPercentage": 100 - ratio,
            "isFree": bool(ratio == 0)
        }

    return promo_element
