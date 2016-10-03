"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j, n, sum, max = 0, 0, len(nums), nums[0], nums[0]
        for i in range(1,n):
            sum  = sum + nums[i] if sum+nums[i] > nums[i] else nums[i]
            max = max if max > sum else sum
        return max
