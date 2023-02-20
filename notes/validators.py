def search_validator(collection, search_data):
    search_match = search_data['search_match']
    date_from = search_data['date_from']
    date_to = search_data['date_to']
    results = None
    if not date_from and not date_to:
        results = collection.filter(text__contains=search_match)
    if date_from and not date_to:
        results = collection.filter(text__contains=search_match).filter(created__gte=date_from)
    if not date_from and date_to:
        results = collection.filter(text__contains=search_match).filter(created__lte=date_to)
    if date_from and date_to:
        results = collection.filter(text__contains=search_match).filter(created__gte=date_from, created__lte=date_to)
    return results
