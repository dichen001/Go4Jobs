"""
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

Hide Company Tags Google
Show Tags
Show Similar Problems

"""


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ans, next = [], lower

        def getRange(l, r):
            return [str(l)] if l == r else [str(l) + '->' + str(r)]

        for n in sorted(set(nums)):
            if n < next:
                continue
            if n == next:
                next += 1
                continue
            ans += getRange(next, n - 1)
            next = n + 1
        if next <= upper:
            ans += getRange(next, upper)
        return ans

