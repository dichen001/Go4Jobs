# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sum(root,0)
    def sum(self,root,tmp):
        if not root:
            return 0
        tmp=tmp*10+root.val
        if root.left==None and root.right==None:
            return tmp
        return self.sum(root.left,tmp)+self.sum(root.right,tmp)
     