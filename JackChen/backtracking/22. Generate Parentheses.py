"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
Hide Company Tags Google Uber Zenefits
Show Tags
Hide Similar Problems
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(left, right, cur):
            if left == 0 and right == 0:
                ans.append(''.join(cur))
            if left > 0:
                backtrack(left-1, right, cur + ['('])
            if right > left:
                backtrack(left, right-1, cur + [')'])
        ans = []
        backtrack(n, n, [])
        return ans
