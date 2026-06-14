#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).
#Example 1:
#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
#Explanation: merged array = [1,2,3] and median is 2.

#Example 2:
#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.50000
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.



#BRUTE FORCE SOLUTION

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l=sorted(nums1+nums2)
        n=len(l)
        result=n%2
        while True:
            if result==0:
                 median=(l[n//2]+l[(n//2)-1])/2
                 print("median of",l,"is",median)
            else:
                median=l[n//2]
                print("median of",l,"is",median)
            
            return median
        

#time complexity:- O((m+n) log(m+n))
#space complexity:- O(m+n)