from src.promotion_utils import get_upcoming_promotional_offers, to_promo_element
from src.slug_utils import to_slug


def to_upcoming_promotion(store_element):
    slug = to_slug(store_element)
    title = store_element["title"]
    promotional_offers = get_upcoming_promotional_offers(store_element)

    all_promo_elements = [
        to_promo_element(slug, title, offer) for offer in promotional_offers
    ]

    return all_promo_elements


def convert_to_promos(store_elements):
    promos = [to_upcoming_promotion(e) for e in store_elements]
    return [p for p in promos if p is not None]
