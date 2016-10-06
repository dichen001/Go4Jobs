"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        ## 3rd. copy from the others.  backward
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal

         ## 2nd try.
        i, reach = 0, 0
        while i < len(nums) and i <= reach and reach < len(nums) -1:
            reach = max(reach, i + nums[i])
            i += 1
        return reach >= len(nums) - 1

        ## first try. Time limit exceeds
        if not nums:
            return False
        if nums[0] >= len(nums) - 1:
            return True
        for i in range(nums[0]):
            if self.canJump(nums[i+1:]):
                return True
        return False