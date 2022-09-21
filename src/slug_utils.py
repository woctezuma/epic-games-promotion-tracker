def get_offer_slug(store_element):
    offers = store_element["offerMappings"]
    if offers is not None and len(offers) > 0:
        offer_slug = offers[0]["pageSlug"]
    else:
        offer_slug = None

    return offer_slug


def get_product_slug(store_element):
    return store_element["productSlug"]


def get_url_slug(store_element):
    return store_element["urlSlug"]


def to_slug(store_element):
    offer_slug = get_offer_slug(store_element)
    product_slug = get_product_slug(store_element)
    url_slug = get_url_slug(store_element)

    if offer_slug is not None:
        slug = offer_slug
    elif product_slug is not None:
        slug = product_slug
    else:
        slug = url_slug

    return slug
