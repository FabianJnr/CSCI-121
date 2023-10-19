def three_prod(number):
    products_list = []
    for first_factor in range(1, number + 1):
        for second_factor in range(first_factor, number + 1):
            for third_factor in range(second_factor, number + 1):
                if first_factor * second_factor * third_factor == number:
                    products_list.append(number)
    return len(products_list)