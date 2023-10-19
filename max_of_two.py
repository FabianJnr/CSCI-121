# def square(number):
#     return number * number
# def cube(number):
#     return number * number * number
    
# def max_of_two(function1, function2, number):
#     return max(function1(number), function2(number))

def make_truncater(number):
    space = number * ''
    b = number
    for char in str(number):
        if len(space) <= b:
            space+=char
