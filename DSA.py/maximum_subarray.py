# problem statment:-  Given an integer array nums, find the subarray with the largest sum, and return its sum.

#solution:-

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        ans,bestending=nums[0],nums[0]

        for i in range(1,len(nums)):

            first_options=bestending+nums[i]
            second_options=nums[i]

            bestending=max(first_options,second_options)

            ans=max(ans,bestending)
        return ans
        

#time complexity:- O(n)
#space complexity:- O(1)
        