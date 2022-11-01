def to_price(store_element):
    try:
        price = store_element["price"]["totalPrice"]["originalPrice"]
    except TypeError:
        price = None

    return price
