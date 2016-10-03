"""
216. Combination Sum III  QuestionEditorial Solution  My Submissions
Total Accepted: 46181
Total Submissions: 115685
Difficulty: Medium
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result, combination, start = [], [], 1
        self.find_all_combination(k, n, result, combination, start)
        return result

    def find_all_combination(self, k, n, result, combination, start):
        if len(combination) == k:
            if n == 0:
                result.append(combination[:])
            return
        while len(combination) < k and start <= n and  start<= 9:
            combination.append(start)
            self.find_all_combination(k, n-start, result, combination, start+1)
            combination.pop()
            start += 1


s = Solution()
s.combinationSum3(3,7)
