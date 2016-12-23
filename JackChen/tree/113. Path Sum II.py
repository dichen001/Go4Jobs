"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root, sum):
            if not root:
                return 
            stack.append(root.val)
            if not root.left and not root.right and root.val == sum:
                ans.append(stack[:])
            else:
                dfs(root.left, sum-root.val)
                dfs(root.right, sum-root.val)
            stack.pop()
        
        ans, stack = [], []
        dfs(root, sum)
        return ans
