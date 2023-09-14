def reversed(number):
    first_number = number // 10
    second_number = number % 10
    output_reversed = second_number * 10 + first_number
    return(output_reversed)