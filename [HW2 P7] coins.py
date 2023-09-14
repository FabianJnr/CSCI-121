def coins(number_of_cents):
    
    number_of_66 = number_of_cents // 66
    number_of_cents = number_of_cents % 66
    
    number_of_6 = number_of_cents // 6
    number_of_cents = number_of_cents % 6
    
    number_of_1 = number_of_cents // 1
   
    return number_of_1 + number_of_6 + number_of_66