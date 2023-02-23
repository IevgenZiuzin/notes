def search_validator(collection, search_data):
    search_match = search_data['search_match']
    date_from = search_data['date_from']
    date_to = search_data['date_to']
    date_match = collection
    if not date_from and not date_to:
        date_match = collection
    if date_from and not date_to:
        date_match = collection.filter(created__gte=date_from)
    if not date_from and date_to:
        date_match = collection.filter(created__lte=date_to)
    if date_from and date_to:
        date_match = collection.filter(created__gte=date_from, created__lte=date_to)
    result = date_match.filter(title__contains=search_match) | date_match.filter(text__contains=search_match)
    return result
