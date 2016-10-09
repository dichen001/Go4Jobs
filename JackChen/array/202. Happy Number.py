"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getNext(n):
            return sum([int(i)**2 for i in str(n)])
        slow, fast = n, n
        while 1:
            slow = getNext(slow)
            fast = getNext(fast)
            fast = getNext(fast)
            if slow == fast:
                break
        return True if slow == 1 else False

        showed = set()
        showed.add(n)
        while 1:
            next = 0
            while n:
                next += (n%10)**2
                n /= 10
            if next == 1:
                return True
            elif next in showed:
                return False
            showed.add(next)
            n = next

