#problem statment:- Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always
#  exists in the array.



# solution:- 

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dic={}
        n=len(nums)
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic:
            if dic[i]>int(n//2):
                return i
        
#time complexity:- O(n)
#space complexity:- O(n)
        


        