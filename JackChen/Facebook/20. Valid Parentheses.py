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
        stack, mem = [], {")":"(", "]":"[", "}":"{"}
        for i, c in enumerate(s):
            if c in "([{":
                stack.append(c)
            elif not stack or stack[-1] != mem[c]:
                return False
            else:
                stack.pop()
        return not stack
