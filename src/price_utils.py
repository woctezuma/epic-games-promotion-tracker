from src.markdown_utils import PRICE_FIELDS

CURRENCY_SYMBOL = '€'


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
    return


def prepare_price_for_display(price_in_cents, currency=CURRENCY_SYMBOL):
    if price_in_cents is None:
        output = 'N/A'
    else:
        price_in_euros = to_units(price_in_cents)
        output = f"{price_in_euros} {currency}".replace('.', ',')
    return output


def to_units(price_in_cents):
    return price_in_cents / 100
