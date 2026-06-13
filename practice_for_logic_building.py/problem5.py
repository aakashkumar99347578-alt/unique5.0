#problem statment:-  Check if a given year is a leap year. 

#solution

def check_leap_year(year):

    if year%4==0:
        print(year,"is a leap year")


    else:
        print(year,"is a not leap year")


check_leap_year(2026)
check_leap_year(2025)
check_leap_year(2024)

