is_even = lambda x: x % 2 == 0

def conditional_print(y):
    def f(x):
        if y(x) == True:
            print(x)
    return f
            
print_evens = conditional_print(is_even)
