#problem statment:-

# Take a number and print whether it’s positive, negative, or zero. 

#solution

def check_number(num):  # create a function with parameter num 
    if num>0:
        print(num,"is a positive number")
    elif num<0:
        print(num,"is a negative number")
    else:
        print(num,"is zero")

check_number(6)
check_number(-8)
check_number(0)