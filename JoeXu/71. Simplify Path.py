class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ss=path.split('/')
        stack=[]
        for s in ss:
            if s=="..":
                if stack!=[]:
                    stack.pop()
            elif s!="." and s!="":
                stack.append(s)
        return "/"+"/".join(stack)