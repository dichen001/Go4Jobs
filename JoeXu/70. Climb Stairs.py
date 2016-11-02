class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #f(n)=f(n-1)+f(n-2)
        res=[1 for i in range(n+1)]

        for i in range(2,n+1):
            res[i]=res[i-1]+res[i-2]
        print(res)
        return res[n]