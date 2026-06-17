# problem statment:- Given an array of integers nums which is sorted in ascending order, and an integer target, write a function 
# to search target in nums. If target exists, then return its index. Otherwise, return -1.You must write an algorithm
#  with O(log n) runtime complexity.



#solution:-

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=int((left+right)/2)
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                return mid
        return -1
        

#time complexity :- O(log(n))
#space complexity:- O(1)