"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def check(s):
            cnt = 0
            for c in s:
                cnt += c == "("
                cnt -= c == ")"
                if cnt < 0:
                    return False
            return cnt == 0
        queue, visited, ans = [s], {s}, []
        found = False
        while queue:
            s = queue.pop(0)
            if check(s):
                ans.append(s)
                found = True
            if found:
                continue
            for i, c in enumerate(s):
                if c not in "()":
                    continue
                t = s[:i] + s[i+1:]
                if t not in visited:
                    visited.add(t)
                    queue.append(t)
        return ans
