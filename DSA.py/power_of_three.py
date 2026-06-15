#problem statment:-  Given an integer n, return true if it is a power of three. Otherwise, return false.
#An integer n is a power of three, if there exists an integer x such that n == 3x.




#solution

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n%3==0:
            n//=3
        return n==1 
        

#time complexity:- O(log(n))
#space complexity:- O(1)