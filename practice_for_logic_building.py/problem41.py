# problem statment Input n and take n integers into an array; print them.


#solution

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("Array elements are:")
for x in arr:
    print(x, end=" ")