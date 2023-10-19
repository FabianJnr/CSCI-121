def char_count(word):
    dictionary = {}
    count = 0
    for i in word:
        dictionary[i] = count
        for j in word:
            if j == i:
                count += 1
                dictionary[i] = count
            else:
                count += 0
                dictionary[i] = count
        count = 0
    return dictionary