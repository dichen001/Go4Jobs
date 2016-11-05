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
        def gen(s, l, r, result):
            if l > 0: gen(s + '(', l-1, r, result)
            if r > l: gen(s + ')', l, r-1, result)
            if not r: result.append(s)
            return result
        result = []
        return gen('', n, n, result)
