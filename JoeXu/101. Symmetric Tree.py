# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root==None:
            return self.f(root.left,root.right)
        return True
    def f(self,l,r):
        if l==None and r==None:
            return True
        if r and l and l.val==r.val:
            return self.f(l.left,r.right) and self.f(l.right,r.left)
        return False