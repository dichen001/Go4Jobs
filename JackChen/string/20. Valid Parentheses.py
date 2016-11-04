"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ls = ['(', '[', '{']
        rs = [')', ']', '}']
        stack = []
        for c in s:
            if c in ls:
                stack.append(c)
            if c in rs:
                if not stack:
                    return False
                t = stack.pop()
                id = ls.index(t)
                if c != rs[id]:
                    return False
        return stack == []
