#problem statment:- Given an array of integers nums sorted in non-decreasing order, find the starting and ending position 
# of a given target value.If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# solution:-

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findFirst():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1   # Continue searching left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def findLast():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1    # Continue searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [findFirst(), findLast()]
    
#time complexity:- O(log(n))
#space complexity:- O(1)
        

 