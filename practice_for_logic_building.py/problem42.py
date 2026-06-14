# problem statment :- Find the sum of all elements in an array.

#solution

n = int(input("how many element want to pass in array : "))
arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

total = 0
for x in arr:
    total += x

print("Sum =", total)