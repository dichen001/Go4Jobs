"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        ### *** my 1st try, sucks...*** ##
        """
        max = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
        return max if max > 0 else 0
        """

        ### *** my 2nd try, still sucks...*** ##
        if not prices:
            return 0
        b_min, s_max = prices[0], 0
        b_id, s_id = 0, 0
        max = 0
        for i, p in enumerate(prices):
            if p < b_min:
                b_min = p
                b_id = i
            if p > s_max:
                s_max = p
                s_id = i
            if s_max - b_min > max and b_id < s_id:
                max = s_max - b_min
            if b_id > s_id:
                s_max = prices[b_id]
        return max

        ### **** other's great solution *****  ###
        min_b, max_p = float('inf'), 0
        for p in prices:
            min_b = min(p, min_b)
            max_p = max(max_p, p - min_b)
        return max_p
