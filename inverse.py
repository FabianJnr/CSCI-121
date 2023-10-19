def inverse(dictionary):
    new_dict = {}
    for value in dictionary.values():
        new_dict[value] = []
    for key, value in dictionary.items():
        new_dict[value].append(key)
    return new_dict