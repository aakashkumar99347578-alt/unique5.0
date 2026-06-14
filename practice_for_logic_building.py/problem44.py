#problem statment :- Find the maximum element in an array. and Find the minimum element in an array.


#solutionn

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

mx = arr[0]

for x in arr:
    if x > mx:
        mx = x

print("Maximum =", mx)

mn = arr[0]

for x in arr:
    if x < mn:
        mn = x

print("Minimum =", mn)
   