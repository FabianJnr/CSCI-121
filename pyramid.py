def pyramid(number):
    p_value = 1
    p_a_shape = ''
    while p_value <= number:
        p_shape = len((number)*' ') - len('*' * p_value)
        spaces = p_shape * ' '
        p_shape = ('* ' * (p_value - 1) + '*')
        p_value = p_value + 1
        p_a_shape = str(p_a_shape) + str(spaces) + str(p_shape) + '\n' 
        
    return p_a_shape