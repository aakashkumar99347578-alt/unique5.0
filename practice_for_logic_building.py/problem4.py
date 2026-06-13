#problem statment:- Check if a number is divisible by both 3 and 5.

#solution

def number_divisible_by_5_and_3(num):  #create a function with for check any number divisible by both 5 and 3

    if num%5 ==0 and num%3==0:                              # check condition number divisible by both 5 and 3
        print(num,"is a number divisible by 5 and 3")


    else:
        print(num,"is not a number divisible by 5 and 3")


number_divisible_by_5_and_3(15)
number_divisible_by_5_and_3(9)

