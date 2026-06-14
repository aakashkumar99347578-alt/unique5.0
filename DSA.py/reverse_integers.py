# problem statment :- Given a signed 32-bit integer x, return x with its digits reversed. If reversing x 
# causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.



#solution 

class Solution:
    def reverse(self, x: int) -> int:
        is_negative=x<0
        absolute_num=str(abs(x))
        rev_num=int(absolute_num[ : : -1])
        if rev_num<-(2**31) or rev_num>(2**31)-1:
            return 0
        else:
            return -(rev_num) if is_negative else rev_num


# time complexity :- O(log(n))
# space complexity :-  O(log(n))