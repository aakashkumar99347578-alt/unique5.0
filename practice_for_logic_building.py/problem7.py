#Take three numbers and print the largest. 

#solution


def largest_number_between_two_number(num1,num2,num3):


    if num1>num2 and num1>num3:
        print(num1,"is a largest number")

    elif num2>num1 and num2>num3:
        print(num2,"is a largest nuumber")

    else:
        print(num3,"is a largest number")

largest_number_between_two_number(58,12,6)
largest_number_between_two_number(12,25,10)
largest_number_between_two_number(17,65,100)