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
        long, longest = 0, [0]
        def dfs(root, pre, long):
            if root:
                if root.val == pre + 1:
                    long += 1
                    longest[0] = max(longest[0], long)
                else:
                    long = 1
                if root.left:
                    dfs(root.left, root.val, long)
                if root.right:
                    dfs(root.right, root.val, long)
        if root:
            long += 1
            longest[0] += 1
            dfs(root.left, root.val, long)
            dfs(root.right, root.val, long)
        return longest[0]