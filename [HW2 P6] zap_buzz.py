def zap_buzz(number):
    integer = number
    multiple_of_7 = number % 7 == 0
    num_contains_3 = 3
    dig_1 = number % 10
    number = number // 10
    dig_2 = number % 10
    number = number // 10
    dig_3 = number % 10
    digits = [dig_1, dig_2, dig_3]
    if multiple_of_7 == True and num_contains_3 in digits:
        return 'zap buzz'
    elif multiple_of_7 == True:
        return 'zap'
    elif num_contains_3 in digits:
        return 'buzz'
    else:
        return integer