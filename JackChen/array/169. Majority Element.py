"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        vote = 0
        for n in nums:
            if vote == 0:
                major = n
            if n == major:
                vote += 1
            else:
                vote -= 1
        return major