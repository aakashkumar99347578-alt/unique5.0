#problem statment:-  Find HCF (GCD) of two numbers using loops. Find LCM of two numbers using loops. 

#solution


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

hcf = 1

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print("HCF =", hcf)



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

max_num = max(num1, num2)

while True:
    if max_num % num1 == 0 and max_num % num2 == 0:
        lcm = max_num
        break
    max_num += 1

print("LCM =", lcm)
