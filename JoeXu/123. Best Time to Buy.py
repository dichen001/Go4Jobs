class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #set a breakpoint i, find max profit before it and min profit after it
        maxP=0
        l=len(prices)
        if l==0: return 0
        p1=[0 for i in range(l)]
        p2=[0 for i in range(l)]
        
        t=prices[0]
        for i in range(1,l):
            t=min(t,prices[i])
            p1[i]=max(p1[i-1],prices[i]-t)
                
        r=prices[l-1]
        for i in range(l-2,-1,-1):
            r=max(r,prices[i])
            p2[i]=max(p2[i+1],r-prices[i])
                
        for i in range(l):
            if p1[i]+p2[i]>maxP:
                maxP=p1[i]+p2[i]
        return maxP