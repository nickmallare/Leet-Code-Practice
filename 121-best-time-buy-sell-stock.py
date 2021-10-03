""" 
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        trade = 0
        lowestBuy = prices[0]

        for trade in prices:
            if trade < lowestBuy:
                lowestBuy = trade;
            else:
                maxProfit = max(maxProfit, trade - lowestBuy)
        return maxProfit

  

a = Solution();
test = [3, 3, 2, 4, 6];
print(a.maxProfit(test))