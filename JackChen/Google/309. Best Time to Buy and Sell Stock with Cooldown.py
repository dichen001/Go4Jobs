"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Space optimazed.
        if not prices:
            return 0
        n = len(prices)
        b0, b1, s0, s1, s2 = 0, -prices[0], 0, 0, 0
        ans = 0
        for i, p in enumerate(prices[1:], 1):
            b0 = max(b1, s2 - p)
            s0 = max(s1, b1 + p)
            b1 = b0
            s2 = s1
            s1 = s0
        return s0

        if not prices:
            return 0
        n = len(prices)
        buy, sell = [0] * n, [0] * n
        buy[0] = -prices[0]
        ans = 0
        for i, p in enumerate(prices[1:], 1):
            buy[i] = max(buy[i - 1], sell[i - 2] - p)
            sell[i] = max(sell[i - 1], buy[i - 1] + p)
        return sell[n - 1]


