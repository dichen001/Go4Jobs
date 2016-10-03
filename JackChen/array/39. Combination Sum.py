"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

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
        result, combination, start = [], [], 0
        candidates.sort(reverse=True)
        self.find_all_combination(candidates, target, result, combination, start)
        return result

    def find_all_combination(self, candidates, target, result, combination, start):
        if target == 0:
            # note it's important to use  [:]  here so that combination.pop() won't modify result.
            result.append(combination[:])
            return
        while start < len(candidates):
            if candidates[start] <= target:
                combination.append(candidates[start])
                self.find_all_combination(candidates, target-candidates[start], result, combination, start)
                combination.pop()
            start += 1


s = Solution()
s.combinationSum([2,3,6,7],7)
