"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        # 2nd copy
        def bi_search(target):
            ### hi = len(nums) - 1 doesn't work for [0], 0 !!!!! very important
            l, h = 0, len(nums)
            while l < h:
                m = (l + h) / 2
                if target <= nums[m]:
                    h = m
                else:
                    l = m + 1
            return l
        left = bi_search(target)
        return [left, bi_search(target+1)-1] if target in nums[left: left+1] else [-1, -1]
        ## doesn't work for [2,2],3
        return [left, bi_search(target+1)-1] if nums[left] == target else [-1, -1]


        # first copy
        r = [-1, -1]
        l, h = 0, len(nums) - 1
        # find lower first
        while l < h:
            m = (l + h) / 2
            if target > nums[m]:
                l = m + 1
            else:
                h = m
        if nums[l] != target:
            return r
        else:
            r[0] = l
        h = len(nums) - 1
        while l < h:
            m = (l + h) / 2 + 1
            if target < nums[m]:
                h = m - 1
            else:
                l = m
        r[1] = l
        return r