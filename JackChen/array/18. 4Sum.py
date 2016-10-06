"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]: continue
            sum_3 = target - nums[i]
            for j in range(i+1, len(nums) -2):
                if  j > i+1 and nums[j] == nums[j-1]: continue
                l, h, sum_2 = j+1, len(nums) - 1, sum_3 - nums[j]
                while l < h:
                    if nums[l] + nums[h] < sum_2:
                        l += 1
                    elif nums[l] + nums[h] > sum_2:
                        h -= 1
                    else:
                        results.append([nums[i], nums[j], nums[l], nums[h]])
                        while l < h and nums[l] == nums[l+1]: l += 1
                        while l < h and nums[h] == nums[h-1]: h -= 1
                        l, h = l+1, h-1
        return results