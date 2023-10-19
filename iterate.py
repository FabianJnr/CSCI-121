def square(x):
    return x * x
def cube(x):
    return x * x * x
def iterate(h, number):
    def g(x):
        value = x
        f = 1
        while f <= number:
            value = h(value)
            f += 1
        return value 
    return g