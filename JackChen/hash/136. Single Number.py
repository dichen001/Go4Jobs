"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for n in nums:
            result ^= n
        return result

        # 1st try
        """
        h = {}
        for n in nums:
            if h.get(n):
                h[n] += 1
            else:
                h[n] = 1
        for n in h.keys():
            if h[n] != 2:
                return n
        """
