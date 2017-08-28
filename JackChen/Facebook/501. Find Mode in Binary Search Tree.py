"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # O(1) Space
        PRE, CUR, MAX, MAX_V = 0, 1, 2, 3
        C = [None, 0, 0, []] # preValue, curCount, maxCount, maxValue
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if node.val == C[PRE]:
                C[CUR] += 1
            else:
                C[CUR] = 1
            if C[CUR] > C[MAX]:
                C[MAX] = C[CUR]
                C[MAX_V] = [node.val]
            elif C[CUR] == C[MAX]:
                C[MAX_V] += [node.val]
            C[PRE] = node.val
            dfs(node.right)
        dfs(root)
        return C[MAX_V]




        # O（N) Space: Counter, Max
