l=[]
n = int(input("how many numbers enter in the arrray "))
for i in range(n):
    number = int(input(" enter the number for array "))
    l.append(number)

print(sum(l))

def sum(l):
    sum=0
    for i in l:
        if i%2==0:
            sum+=i
    return sum

def countoccurneces(arr,target):
    count=0
    for i in arr:
        if i == target:
            count+=1
    return count

def reverse(arr):
    return arr[ : :-1]

def posinge(arr):
    possum=0
    ingsum =0
    for i in arr:
        if i ==0:
            continue
        elif i>0:
            possum+=i
        else:
            ingsum+=i
    return possum,ingsum

print("all positive and negative sum", posinge(arr=[5,15,-5,-73,30,0,48,-25]))

def all():
    print(countoccurneces(arr,target))
    print("reverser o the array ",reverse(arr))


size = int(input("enter the size of array"))
arr = []
for i in range(size):
    number = int(input(f"enter the element ar index {i} "))
    arr.append(number)

target = int(input("enter the target element"))
all()
