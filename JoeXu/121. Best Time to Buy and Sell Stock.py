class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=len(prices)
        if l<=1:
            return 0
        maxP=0
        t=prices[0]
        for i in range(l):
            if t>prices[i]:
                t=prices[i]
            else:
                maxP=max(maxP,prices[i]-t)
        return maxP