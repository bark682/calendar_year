def leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                is_leap = True
            else:
                is_leap = False
        else:
            is_leap = True
    else:
        is_leap = False 
    
    return is_leap

    