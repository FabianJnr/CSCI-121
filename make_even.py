def make_even(prev_list):
    for number in range(len(prev_list)):
        if prev_list[number] % 2 != 0:
            prev_list[number] -= 1