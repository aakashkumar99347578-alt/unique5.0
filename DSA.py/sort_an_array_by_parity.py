#problem statment:- Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
#Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
#Return any answer array that satisfies this condition.




#solution:-

class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n=len(nums)
        i,j=0,1
        while i<n and j<n:
             while i < n and nums[i] % 2 == 0:
                i += 2
             while j<n and nums[j]%2==1:
                j+=2
             if i<n and j<n:
                nums[i],nums[j]=nums[j],nums[i]
        return nums