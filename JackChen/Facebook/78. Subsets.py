"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # iterative
        ans = [[]]
        for n in nums:
            size = len(ans)
            for i in range(size):
                ans.append(ans[i] + [n])
        return ans

        # recursive
        def backtrack(start, cur):
            ans.append(cur[:])
            for i in range(start, len(nums)):
                backtrack(i + 1, cur + [nums[i]])

        ans = []
        backtrack(0, [])
        return ans

