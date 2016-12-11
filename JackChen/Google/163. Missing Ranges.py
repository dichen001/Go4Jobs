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
        if not nums:
            return [str(lower)] if lower == upper else[str(lower) + '->' + str(upper)]
        ranges = []
        pre = lower - 1
        nums = sorted(set(nums))
        for n in nums + [upper + 1]:
            if n not in [pre, pre+1]:
                end = n - 1
                if pre + 1 == end:
                    ranges.append(str(end))
                else:
                    ranges.append(str(pre+1) + '->' + str(end))
            pre = n
        return ranges
