"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums

        i, result = 0, []
        while i < len(nums):
            tmp = nums[i]
            while i+1<len(nums) and nums[i+1]==nums[i]+1:
                i += 1
            if nums[i] == tmp:
                result.append(str(nums[i]))
            else:
                result.append(str(tmp) + '->' +str(nums[i]))
            i += 1
        return result
