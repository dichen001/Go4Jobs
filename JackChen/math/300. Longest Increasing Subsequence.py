"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_tails = [0] * len(nums)
        size = 0
        for n in nums:
            left, right = 0, size
            while left != right:
                m = (left + right) / 2
                if min_tails[m] < n:
                    left = m + 1
                else:
                    right = m
            min_tails[left] = n
            size = max(size, left + 1)
        return size
