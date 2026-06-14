# problem statment :- You are given a 0-indexed array nums consisting of positive integers.
#You can do the following operation on the array any number of times:



# solution

class Solution:
    def maxArrayValue(self, nums: list[int]) -> int:
        curr = nums[-1]
        ans = curr

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= curr:
                curr += nums[i]
            else:
                curr = nums[i]

            ans = max(ans, curr)
 
        return ans
    


# time complexity:- O(n)
# space complexity :- O(1)