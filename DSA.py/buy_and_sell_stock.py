#problem statmet:-  You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



#solution:-


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum_price=prices[0]
        max_profit=0
        for i in range (1,len(prices)):

            minimum_price=min(minimum_price,prices[i])

            max_profit=max(max_profit,prices[i]-minimum_price)
        return max_profit
    


#time complexity:- O(n)
#space complexity:- O(1)
