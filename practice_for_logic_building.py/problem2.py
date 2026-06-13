#problem statment:- Check if a number is even or odd. 

#solution

def check_even_odd(num):  # create a function for check even odd number with parameter num

    if num%2==0:                             # check num is even by if condition
        print(num,"is a even number")


    else:
        print(num,"is a odd number")

check_even_odd(4)
check_even_odd(3)
