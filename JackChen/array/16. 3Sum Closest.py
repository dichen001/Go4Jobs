"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        close = float("inf")
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, h = i + 1, len(nums) - 1
            while l < h:
                sub = nums[i] + nums[l] + nums[h]
                close = sub if abs(target - sub) < abs(target - close) else close
                if target > sub:
                    l += 1
                elif target < sub:
                    h -= 1
                else:
                    return target
        return close

s = Solution()
s.threeSumClosest([-4, -1, 1, 2], 1)