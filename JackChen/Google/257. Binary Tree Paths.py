"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def dfs(root):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                ans.append('->'.join([str(p) for p in path]))
            dfs(root.left)
            dfs(root.right)
            path.pop()
        path, ans = [], []
        dfs(root)
        return ans
