"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        mem = set()
        for n in nums:
            if n > 0:
                mem.add(n)
        for i in range(1, len(nums) + 1):
            if i not in mem:
                return i
        return i + 1
