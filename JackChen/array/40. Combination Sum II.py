"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
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
        for i in range(start, len(candidates)):
            if candidates[i] <= target and (i==start or candidates[i] != candidates[i-1]):
                combination.append(candidates[i])
                self.find_all_combination(candidates, target-candidates[i], result, combination, i+1)
                combination.pop()
