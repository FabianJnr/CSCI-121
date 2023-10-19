def conditional_print(y):
    def f(x):
        if y(x) == True:
            print(x)
    return f