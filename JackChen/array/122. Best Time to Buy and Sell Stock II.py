"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like

(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time

(ie, you must sell the stock before you buy again).
"""

# solusion if we could buy and sell at the same day.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


# solusion if we could NOT buy and sell at the same day.
    def maxProfit2(prices):
        profit = i = 0
        while i < len(prices):
            # Find local minima
            while i < len(prices)-1 and prices[i+1] <= prices[i]:
                i += 1
            minima = prices[i]
            i += 1

            # Find local maxima
            while i < len(prices)-1 and prices[i+1] >= prices[i]:
                i += 1
            if i < len(prices):
                profit += prices[i] - minima
            else:
                profit += 0

        return profit
