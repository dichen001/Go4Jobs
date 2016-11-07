"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n, result = len(prices), 0
        mem = [0] * n
        min_b1, max_p1 = float('inf'), 0
        max_s, max_p = 0, 0
        for i, p in enumerate(prices[::-1]):
            max_s = max(max_s, p)
            max_p = max(max_p, max_s - p)
            mem[n-i-1] = max_p
        for day, p1 in enumerate(prices):
            min_b1 = min(p1, min_b1)
            max_p1 = max(max_p1, p1 - min_b1)
            result = max(max_p1 + mem[day], result)
        return result



s = Solution()
s.maxProfit([3,3,5,0,0,3,1,4])
