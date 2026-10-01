arr = [1,23,5,6]
target = 6


def arraysum(arr,target):
    left =0
    right =len(arr)-1
    while left<right:
        if arr[left]+arr[right]==target:
            return left ,right
        elif arr[left]+arr[right]>target:
            right-=1
        else:
            left+=1
    return -1  
print(arraysum(arr,target))