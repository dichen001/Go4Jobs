"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum = [0] * (1 + len(nums))
        for i, n in enumerate(nums):
            self.sum[i + 1] = self.sum[i] + n

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum[j + 1] - self.sum[i]



        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)