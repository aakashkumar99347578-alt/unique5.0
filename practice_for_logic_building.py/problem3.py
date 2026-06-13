#problem statment:- Check if a number is divisible by 5.

#solution

def number_divisible_by_5(num):  #create a function with parameter num for check num is divisible ny 5 yes or no

    if num %5 ==0:                      # check num divisible by 5
        print(num,"is divisible by 5")

    else:
        print(num,"is not divisible by 5")

number_divisible_by_5(10)
number_divisible_by_5(13)