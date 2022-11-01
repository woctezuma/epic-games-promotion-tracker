from src.price_utils import to_price
from src.promotion_utils import get_upcoming_promotional_offers, to_promo_element
from src.slug_utils import to_slug


def extract_upcoming_promos_from_single_element(store_element):
    slug = to_slug(store_element)
    title = store_element["title"]
    price = to_price(store_element)
    promotional_offers = get_upcoming_promotional_offers(store_element)

    all_promo_elements = [
        to_promo_element(slug, title, price, offer) for offer in promotional_offers
    ]

    return all_promo_elements


def extract_upcoming_promos_from_several_elements(store_elements):
    promos = []
    for e in store_elements:
        promos += extract_upcoming_promos_from_single_element(e)

    return promos
