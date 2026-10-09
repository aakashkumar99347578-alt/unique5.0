arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
maximum = arr[0][0]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j]>maximum:
            maximum= arr[i][j]

print(maximum)



minimum = arr[0][0]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j]<minimum:
            miniimum= arr[i][j]

print(minimum)


arr1 = [
    [1,2,10,14],
    [20,3,25,28],
    [40,5,38,24],
    [25,31,16,12]
]
target = 20
for i in range(len(arr1)):
    for j in range(len(arr1)):
        if target == arr1[i][j]:
            print("index position" ,i,j)  
            break 




