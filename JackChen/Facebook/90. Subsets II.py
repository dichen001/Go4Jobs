"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # iterative
        ans = [[]]
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                start = size
            else:
                start = 0
            size = len(ans)
            for j in range(start, size):
                ans.append(ans[j] + [n])
        return ans

        # recursive
        def backtrack(start, cur):
            ans.append(cur[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                backtrack(i + 1, cur + [nums[i]])

        ans = []
        nums.sort()
        backtrack(0, [])
        return ans