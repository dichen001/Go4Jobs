"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k >= n/2:
            return sum([max(0, prices[i+1] - prices[i]) for i in range(n-1)])
        dp = [[0] * n for _ in range(k + 1)]
        result = 0
        for i in range(1, k+1):
            preMax = - prices[0]
            for j, p in enumerate(prices[1:], 1):
                dp[i][j] = max(dp[i][j-1], preMax + p)
                preMax = max(preMax, dp[i-1][j] - p)
        return dp[k][n-1]
