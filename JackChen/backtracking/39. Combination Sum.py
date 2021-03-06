"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(path, cur, s):
            if cur == target:
                ans.append(path)
            elif cur < target:
                for i, n in enumerate(candidates[s:], s):
                    dfs(path + [n], cur + n, i)

        ans = []
        dfs([], 0, 0)
        return ans



        def backtrack(tmp, start, end, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    tmp.append(candidates[i])
                    backtrack(tmp, i, end, target - candidates[i])
                    tmp.pop()
        ans = []
        candidates.sort(reverse= True)
        backtrack([], 0, len(candidates), target)
        return ans

s = Solution()
s.combinationSum([2,3,6,7], 7)
