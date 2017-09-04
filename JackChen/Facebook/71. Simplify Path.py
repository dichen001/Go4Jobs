"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = path.split('/')
        ans = [""]
        for s in stack:
            if not s or s == ".":
                continue
            elif s == "..":
                if len(ans) > 1:
                    ans.pop()
            else:
                ans.append(s)
        return "/" + "/".join(ans)[1:]