"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 3rd. Recursive
        if root in [None, p, q]:
            return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in [root.left, root.right])
        return root if left and right else left or right

        # 2nd try. iterative use O(N) space to save hash.
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q

        # 1st try. Memory Limit Exceeds 29/31 passed.
        # find the path for p and q O(N)
        def dfs(path, node):
            if not node or len(paths) > 1:
                return
            if node in (p, q):
                paths.append(path + [node])
            dfs(path + [node], node.left)
            dfs(path + [node], node.right)

        paths = []
        dfs([], root)
        path0, path1 = paths[0][::-1], set(paths[1])
        for node0 in path0:
            if node0 in path1:
                return node0
        return root