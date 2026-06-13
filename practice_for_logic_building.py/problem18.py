#problem statment:-  Take a day number (1–7) and print the corresponding day name. 



#solution


def get_day(day_num):

    
    if day_num == 1:
        return "Monday"
    
    elif day_num == 2:
        return "Tuesday"
    
    elif day_num == 3:
        return "Wednesday"
    
    elif day_num == 4:
        return "Thursday"
    
    elif day_num == 5:
        return "Friday"
    
    elif day_num == 6:
        return "Saturday"
    
    elif day_num == 7:
        return "Sunday"
    
    else:
        return "Invalid day number"
