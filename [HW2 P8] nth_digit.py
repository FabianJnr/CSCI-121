def nth_digit(x, n):
    num_place_digit = x % (10 ** n)
    num_place_digit = num_place_digit // (10 ** (n-1))
    return num_place_digit