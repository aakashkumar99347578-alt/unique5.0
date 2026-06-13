#problem statment:- take a 3-digit number and check if all digits are distinct.


#solution

num = input("Enter a 3-digit number: ")

if len(set(num)) == 3:
    print("All digits are distinct")

    
else:
    print("Digits are not distinct")