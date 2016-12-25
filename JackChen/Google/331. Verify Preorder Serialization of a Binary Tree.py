class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for c in preorder.split(','):
            stack.append(c)
            while stack[-2:] == ['#', '#']:
                stack.pop()
                stack.pop()
                if not stack:
                    return False
                else:
                    stack[-1] = '#'
        return len(stack) == 1 and stack[0] == '#'
    
s = Solution()
s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
