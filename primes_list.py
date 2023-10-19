def primes_list(number):
    list_of_primes = []
    start_prime = 2
    while len(list_of_primes) < number:
        count = 0
        for i in range(1, start_prime+1):
            if start_prime % i == 0:
                count += 1
        if count == 2:
            list_of_primes.append(start_prime)
        start_prime += 1     
    return list_of_primes 