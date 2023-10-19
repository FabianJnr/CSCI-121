def down_up(number):
    
    n = number 
    list_of_numbers = []
    while n > 0:
        list_of_numbers.append(n)
        n -= 1
    
    for num in range(2, number+1):
        list_of_numbers.append(num)
    return list_of_numbers