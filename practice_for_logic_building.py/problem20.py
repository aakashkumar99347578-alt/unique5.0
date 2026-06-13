#problem statment :-  Take  3-digit number and determine if the middle digit is the largest, smallest, or 
#neither.



#solution

num = int(input("Enter a 3-digit number: "))

a = num // 100        
b = (num // 10) % 10  
c = num % 10          

if b > a and b > c:
    print("The middle digit is the largest.")
elif b < a and b < c:
    print("The middle digit is the smallest.")
else:
    print("The middle digit is neither the largest nor the smallest.")