def numpal(number):
    original_num = number
    num = 0
    while number>0:
        mod_remain = number % 10
        num_place = 10 ** (len(str(number)) - 1)
        num += mod_remain * num_place
        number = number - mod_remain
        int_remain = number // 10
        number = int_remain
    if num == original_num:
        return True
    else:
        return False
    
print(numpal(77777))