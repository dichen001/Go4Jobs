"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i == 0 or nums[i-1] != nums[i]:
                l, r, target = i + 1, len(nums)-1, 0 - nums[i]
                while l < r:
                    if nums[l] + nums[r] == target:
                        ans.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l+1] == nums[l]:
                            l += 1
                        while l < r and nums[r-1] == nums[r]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
        return ans