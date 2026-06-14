# problem statment:-  Find the sum of digits of a number


#solution

num = int(input("Enter a number: "))

sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print("Sum of digits =", sum_digits)