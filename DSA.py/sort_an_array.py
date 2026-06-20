# problem statment:- Given an array of integers nums, sort the array in ascending order and return it.You must solve the problem 
# without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.





# solution:- 

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        return merge_sort(nums)
        