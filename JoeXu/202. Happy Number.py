class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numSet = set()
        while n != 1 and n not in numSet:
            numSet.add(n)
            sum = 0
            while n:
                digit = n % 10
                sum += digit * digit
                n /= 10
            n = sum
        return n==1