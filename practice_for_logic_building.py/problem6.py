#problem statment:- Take two numbers and print the larger one. 

#solution

def largest_number_between_two_number(num1,num2):


    if num1>num2:
        print(num1,"is a largest number between",num1,"and",num2)

    else:
        print(num2,"is a largest number between",num1,"and",num2)

largest_number_between_two_number(58,12)
largest_number_between_two_number(12,25)