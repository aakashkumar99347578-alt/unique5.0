#problem statment:- Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result
#  must be unique and you may return the result in any order.


#solution


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        num1=set(nums1)
        num2=set(nums2)
        my_list=[]
        for num in num1:
            if num in num2:
                my_list.append(num)
        return my_list 
