#problem statment:-  Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# solution:-  

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n

        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        
        reverse(0,n-1)
        reverse(0, k - 1)      
        reverse(k, n - 1)  


#time complexity:- O(n)
#space complexity:- O(1)

