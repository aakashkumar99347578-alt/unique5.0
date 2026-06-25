#problem statment:-  Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times


#solution:- 

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        dic={}
        new_list=[]
        n=len(nums)
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic:
            if dic[i]>int(n/3):
                new_list.append(i)
        
        return new_list
        


   
#time complexity:- O(n)
#space complexity:- O(n)
        