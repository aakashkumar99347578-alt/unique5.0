# problem statment :-Check if one of two given numbers is a multiple of the other. 


# solution

def is_multiple(a, b):
    if a % b == 0 or b % a == 0:
        return True
    return False

# Input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Check
if is_multiple(num1, num2):
    print("One number is a multiple of the other.")
else:
    print("Neither number is a multiple of the other.")