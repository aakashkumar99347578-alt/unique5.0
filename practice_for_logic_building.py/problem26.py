#problem statment:-  Print all even and odd also sum of all even and odd numbers between 1 and 100.


#solution

sum_even=0
sum_odd=0

for num in range (1,101):
    if num%2==0:
        print(num,"is even number")
        sum_even+=num
    else:
        print(num,"is a odd number")
        sum_odd+=num

print(sum_even)
print(sum_odd)