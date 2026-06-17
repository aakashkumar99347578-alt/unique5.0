#problem statment:- Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums 
# such that the sum is closest to target.Return the sum of the three integers.


#solution:-

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = []
        n = len(nums)
        max_diff=float('inf')
        result=0

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]
                diff=abs(total-target)
                if diff<max_diff:
                    max_diff=diff
                    result=total

                if total < target:
                    left += 1

                elif total > target:
                    right -= 1

                else:
                    left  += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
