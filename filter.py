def filter(a, b):
    new_list = []
    for number in b:
        if a(number) == True:
            new_list.append(number)
    return new_list