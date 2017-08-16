"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
Show Company Tags
Show Tags
Show Similar Problems

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, val, cur_len):
            if not node:
                return cur_len
            cur_len = cur_len + 1 if node.val == val + 1 else 1
            left = dfs(node.left, node.val, cur_len)
            right = dfs(node.right, node.val, cur_len)
            return max(cur_len, left, right)
        
        return dfs(root, root.val, 1) if root else 0
            
        
        
        