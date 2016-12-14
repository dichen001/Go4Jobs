"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].

Hint:

Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.
"""

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def getAll(m, n):
            if m == 0: return ['']
            if m == 1: return ['0', '1', '8']
            smaller = getAll(m-2, n)
            all = []
            for s in smaller:
                # when m == n, i.e. the most outer 2 number, we cannot do '0xxx0' ---> 'xxx'
                if m != n:
                    all += ['0' + s + '0']
                for p in [('1', '1'), ('6', '9'), ('9', '6'), ('8', '8')]:
                    all += [p[0] + s + p[1]]
            return all
        return getAll(n,n)
