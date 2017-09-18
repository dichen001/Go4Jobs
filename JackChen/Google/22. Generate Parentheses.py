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
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(path, l, r):
            if l == r == 0:
                ans.append(''.join(path))
            elif l == r:
                dfs(path + ["("], l - 1, r)
            elif l < r:
                if l > 0:
                    dfs(path + ["("], l - 1, r)
                dfs(path + [")"], l, r - 1)

        ans = []
        dfs([], n, n)
        return ans