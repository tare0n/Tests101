def get_val(collection, key, default='world'):
    if isinstance(collection, dict) and collection != {}:
        return collection[key]
    else:
        return default


print(get_val({"hello": "world"}, "hello"))
print(get_val({"hello": "world"}, "hello", "python"))  
print(get_val({}, "hello", "python"))