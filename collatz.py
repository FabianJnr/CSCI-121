def collatz(n):
    def list_controller(num):
        list_of_numbers = []
        list_of_numbers.append(num)
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                list_of_numbers.append(num)
            else:
                num % 2 != 0
                num = (num * 3) + 1
                list_of_numbers.append(num)
        return len(list_of_numbers)
            

    end_point = 1
    while list_controller(end_point) < n:
        end_point+=1
          
    return end_point

