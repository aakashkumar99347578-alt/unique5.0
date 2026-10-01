number = int(input("enter the number "))
original = number
rev = 0
while number>0:
    rem = number%10
    rev = rev*10 +rem
    number = number//10
if original==rev:
    print("Yes this number is palidrom")
else:
    print("No this number is not a palidrom ")

