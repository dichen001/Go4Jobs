ass Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            result=1/self.myPow(x,-n)
        else:
            temp=self.myPow(x,n//2)
            if n%2==0:
                result=temp*temp
            else:
                result=temp*temp*x
        return result
