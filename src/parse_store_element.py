from src.promotion_utils import get_upcoming_promotional_offers, to_promo_element
from src.slug_utils import to_slug


def to_upcoming_promotion(store_element):
    promotional_offers = get_upcoming_promotional_offers(store_element)

    if promotional_offers is None:
        promo_element = None
    else:
        first_promotional_offer = promotional_offers[0]
        if len(promotional_offers) > 1:
            print(promotional_offers)  # TODO

        slug = to_slug(store_element)

        promo_element = to_promo_element(slug, store_element["title"], first_promotional_offer)

    return promo_element


def convert_to_promos(store_elements):
    promos = [to_upcoming_promotion(e) for e in store_elements]
    return [p for p in promos if p is not None]
