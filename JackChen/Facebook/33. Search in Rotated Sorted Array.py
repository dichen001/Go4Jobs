"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) / 2
            if target == nums[m]:
                return m
            # left side is sorted:
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right side is sorted:
            if nums[m] <= nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


        n = len(nums)
        l, r = 0, n
        while l < r:
            m = (l + r) / 2
            if (nums[m] < nums[0]) == (target < nums[0]):
                n = nums[m]
            else:
                n = float("-inf") if target < nums[0] else float("inf")
            if target > n:
                l = m + 1
            elif target < n:
                r = m
            else:
                return m
        return -1