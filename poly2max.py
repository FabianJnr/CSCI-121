def poly2max(x_min, x_max, y_min, y_max):
    z = -(x_min**4) + (3 * x_min**2) - (y_min**4) + (5*y_min**2)
    
    x = x_min
    while x <= x_max:
        y = y_min
        while y <= y_max:
            z = max(z, ((-(x**4)) + (3*x**2) - (y**4) + (5*y**2)))
            y += 1
        x += 1
    return z

print(poly2max(0, 5, 0, 10))