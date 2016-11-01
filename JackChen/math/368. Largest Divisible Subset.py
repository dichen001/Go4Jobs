"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        T, parent = [0] * n, [0] * n
        size, trace_id = 0, 0
        for i in range(n):
            for j in range(i, -1, -1):
                if nums[i] % nums[j] == 0 and T[i] < T[j] + 1:
                    T[i] = T[j] + 1
                    parent[i] = j
                if T[i] > size:
                    size, trace_id = T[i], i
        result = []
        for i in range(size):
            result.append(nums[trace_id])
            trace_id = parent[trace_id]
        result.sort()
        return result
