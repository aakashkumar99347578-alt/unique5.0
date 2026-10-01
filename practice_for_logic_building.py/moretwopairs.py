arr = [0,1,2,3,4,5,6]
target = 6


def arraysum(arr,target):
    left =0
    right =len(arr)-1
    count=0
    while left<right:
        if arr[left]+arr[right]==target:
            count+=1
            left+=1
            right-=1
        elif arr[left]+arr[right]>target:
            right-=1
        else:
            left+=1
    return count
print(arraysum(arr,target))