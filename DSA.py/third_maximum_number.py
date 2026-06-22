#problem statment:- Given integer array nums, return the third distinct maximum number in this array. If the third maximum 
# does not exist, return the maximum number

# .Constraints:

#1 <= nums.length <= 104
#-231 <= nums[i] <= 231 - 1
 
#Follow up: Can you find an O(n) solution?




#solution:-

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = second = third = float('-inf')

        for num in nums:
            if num == first or num == second or num == third:
                continue

            if num > first:
                third = second
                second = first
                first = num

            elif num > second:
                third = second
                second = num

            elif num > third:
                third = num

        return first if third == float('-inf') else third


