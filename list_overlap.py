def list_overlap(first_lst, second_lst):
    second_copy = second_lst[:]
    new_lst = []
    for value1 in first_lst:
        for value2 in second_copy:
            if value1==value2:
                new_lst.append(value1)
                second_copy.remove(value2)
                break
    return new_lst