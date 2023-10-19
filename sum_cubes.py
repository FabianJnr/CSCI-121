def sum_cubes(n):
    if n < 1:
        return 0
    
    cubes = 0
    number = 1
    while n >= number:
        operations = number ** 3
        cubes = operations + cubes
        number = number + 1 
    return cubes