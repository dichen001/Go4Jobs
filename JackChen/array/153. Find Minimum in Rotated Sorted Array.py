"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l+h)/2
            if nums[m] < nums[h]:
                h = m
            else:
                l = m + 1
        return nums[l]


