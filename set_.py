def set_(coll, path, value=0):
    out_string = '{'
    for letter in path[:-1]:
        out_string += f'"{letter}": '
        out_string += '{'
    out_string += f'"{path[-1]}": {value}'
    for i in range(len(path)):
        out_string += '}'
    out_dict = eval(out_string)
    coll.update(out_dict)


set_({"a": {"b": {"c": 4}}}, ["a", "b", "c"], 6)




