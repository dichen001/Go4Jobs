"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        if len(nums) < 2:
            return 0
        for i in range(len(nums)):
            if i == 0 and nums[0] > nums[1]:
                return i
            if i == len(nums)-1 and nums[-1] > nums[-2]:
                return i
            if nums[i] > nums[i-1] and nums[i]>nums[i+1]:
                return i
        return 0
        """

        l, h = 0, len(nums)-1
        while l < h:
            m = (l+h)/2
            if nums[m] > nums[m+1]:
                h = m
            else:
                l = m + 1
        return l