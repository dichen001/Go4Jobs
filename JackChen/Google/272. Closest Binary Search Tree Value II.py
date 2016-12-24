"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

Hint:

Consider implement these two helper functions:
getPredecessor(N), which returns the next smaller node to N.
getSuccessor(N), which returns the next larger node to N.
Try to assume that each node has a parent pointer, it makes the problem much easier.
Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
You would need two stacks to track the path in finding predecessor and successor node separately.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def dfs(node, target, reverse):
            if not node:
                return
            if reverse:
                dfs(node.right, target, reverse)
                if node.val <= target:
                    return
                suc.append(node.val)
                dfs(node.left, target, reverse)
            else:
                dfs(node.left, target, reverse)
                if node.val > target:
                    return
                pre.append(node.val)
                dfs(node.right, target, reverse)
        ans, pre, suc = [], [], []
        dfs(root, target, True)
        dfs(root, target, False)
        for i in range(k):
            if not pre:
                ans += [suc.pop()]
            elif not suc:
                ans += [pre.pop()]
            elif abs(pre[-1] - target) < abs(suc[-1] - target):
                ans += [pre.pop()]
            else:
                ans += [suc.pop()]
        return ans
