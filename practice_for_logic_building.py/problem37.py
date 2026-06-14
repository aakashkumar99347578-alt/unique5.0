#problem statment :- Print first n terms of an arithmetic progression (a, d). 


#solution

a = int(input("Enter first term (a): "))
d = int(input("Enter common difference (d): "))
n = int(input("Enter number of terms (n): "))

for i in range(n):
    term = a + i * d
    print(term, end=" ")
