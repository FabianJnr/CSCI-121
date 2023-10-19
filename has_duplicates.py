def has_duplicates(ls):
    count = 0
    for number in range(len(ls)):
        if ls[number] in ls[number+1:] or ls[number] in ls[:number]:
            count += 1
    if count > 0:
        return True
    else:
        return False