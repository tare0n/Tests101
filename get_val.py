def get_val(collection, key, default='world'):
    if isinstance(collection, dict) and collection != {}:
        return collection[key]
    else:
        return default
