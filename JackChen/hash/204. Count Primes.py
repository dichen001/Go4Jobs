"""
Description:

Count the number of prime numbers less than a non-negative number, n.
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        isPrime = [False]*2 + [True] * (n-2)
        for i in range(2, int(n**0.5)+1, 1):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
        return sum(isPrime)




s = Solution()
s.countPrimes(100)
