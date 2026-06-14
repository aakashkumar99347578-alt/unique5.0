#problem statment:- average of elment in array 


#solution

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

total = 0
for x in arr:
    total += x

avg = total / n
print("Average =", avg)