# create an array an copy the all number in other aaray but all element position are reverse 

size = int(input("enter the size of array"))
l=[]
for i in range(1,size+1):
    number = int(input(f"enter the number at index {i} "))
    l.append(number)

def copyarray(arr):
    br =[]
    for i in (arr[: :-1]):
        br.append(i)
    return br

print(copyarray(l))