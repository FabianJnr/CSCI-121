def square(x):
    return x * x
def cube(x):
    return x * x * x
def max_of_funcs(f, g):
    def h(x):
        return max(f(x), g(x))
    return h