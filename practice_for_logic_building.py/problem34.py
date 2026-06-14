#problem statment:- Print Fibonacci series up to n terms.  Print sum of first n terms of Fibonacci series. 


#solution

# print fibonacci series up to n terms 


n = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


#print sum of first n trms of fibonacci series

n = int(input("\nEnter number of terms: "))

a, b = 0, 1
sum_fib = 0

for i in range(n):
    sum_fib += a
    a, b = b, a + b

print("Sum =", sum_fib)