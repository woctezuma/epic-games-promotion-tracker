def unique(data):
    # Return a list of unique elements, preserving order.
    unique_data = []
    for element in data:
        if element not in unique_data:
            unique_data.append(element)
    return unique_data
