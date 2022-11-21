from src.markdown_utils import MISSING_DATA, PRICE_FIELDS

CURRENCY_SYMBOL = "€"


def to_price(store_element):
    try:
        price = store_element["price"]["totalPrice"]["originalPrice"]
    except TypeError:
        price = None

    return price


def format_prices_for_display(data):
    for entry in data:
        format_prices_in_dict(entry)

    return data


def format_prices_in_dict(entry):
    for k in PRICE_FIELDS:
        entry[k] = prepare_price_for_display(entry[k])


def prepare_price_for_display(price_in_cents: int | None, currency: str = CURRENCY_SYMBOL) -> str:
    if price_in_cents is None or price_in_cents < 0:
        output = MISSING_DATA
    else:
        price_in_euros = to_units(price_in_cents)
        output = f"{price_in_euros:.2f}{currency}".replace(".", ",")
    return output


def to_units(price_in_cents: int) -> float:
    return price_in_cents / 100


def to_price_int(price_str: str, currency: str = CURRENCY_SYMBOL) -> int:
    price_in_euros = price_str.replace(currency, "")
    price_in_cents = price_in_euros.replace(".", "").replace(",", "")
    try:
        price_as_int = int(price_in_cents)
    except ValueError:
        price_as_int = -1
    return price_as_int
