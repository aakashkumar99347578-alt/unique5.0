#problem statment:-  Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

#solution:-  

class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        ans=0
        while left<=right:

            mid=int((left+right)//2)

            if mid*mid==x:

                return mid

            elif mid*mid>x:

                right=mid-1
            else:
                ans=mid
                left=mid+1

        return ans
    

#time complexity:- O(log(n))
#space complexity:- O(1)
 