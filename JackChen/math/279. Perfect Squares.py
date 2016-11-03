"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

"""

# BFS search as illustrated here: https://discuss.leetcode.com/topic/26262/short-python-solution-using-bfs/2
# https://discuss.leetcode.com/uploads/files/1467720855285-xcoqwin.png
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        count, tocheck = 0, [n]
        while tocheck:
            count += 1
            next_tocheck = set()
            for check in tocheck:
                for s in squares:
                    if s == check:
                        return count
                    if s > check:
                        break
                    next_tocheck.add(check-s)
            tocheck = next_tocheck
        return count
