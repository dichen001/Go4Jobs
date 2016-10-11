class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxP=0
        l=len(prices)
        for i in range(l-1):
            if prices[i]<prices[i+1]:
                maxP=maxP-prices[i]+prices[i+1]
        return maxP
            