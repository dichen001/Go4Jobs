"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        # first try:   Time Limit Exceeded
        i = 0
        while i < len(nums)-1:
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i , j]
                j += 1
            i += 1
        return none
        """
        
        i = 0
        hash = {}
        while i < len(nums):
            if nums[i] not in hash:
                hash[target-nums[i]] = i
                i += 1
            else:
                return hash[nums[i]], i
