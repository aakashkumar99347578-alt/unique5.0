#problem statment:-Take a 4-digit number and check if the first and last digits are equal. 


#solution

num = int(input("Enter a 4-digit number: "))

first = num // 1000   
last = num % 10    

if first == last:
    print("The first and last digits are equal.")


else:
    print("The first and last digits are not equal.")