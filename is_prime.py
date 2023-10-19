def is_prime(n):
    if n < 2:
        return False
    num_divisor = 2
    while n > num_divisor:
        if n % num_divisor == 0:
            return False
        else:
            num_divisor = num_divisor + 1
    return True