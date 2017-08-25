"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
return its vertical order traversal as:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        ans, mem = [], {}

        # doesn't work cause top one should before lower ones.
        # to do that, we need to use BFS.
        #         def dfs(node, diff):
        #             if not node:
        #                 return
        #             if diff in mem:
        #                 mem[diff].append(node.val)
        #             else:
        #                 mem[diff] = [node.val]
        #             dfs(node.left, diff - 1)
        #             dfs(node.right, diff + 1)
        #         dfs(root, 0)

        queue = collections.deque([(root, 0)])
        while queue:
            node, diff = queue.popleft()
            if diff not in mem:
                mem[diff] = [node.val]
            else:
                mem[diff].append(node.val)
            if node.left:
                queue.append((node.left, diff - 1))
            if node.right:
                queue.append((node.right, diff + 1))
        for i in sorted(mem.keys()):
            ans.append(mem[i])
        return ans


r = TreeNode(3)
r.left = TreeNode(9)
r.right = TreeNode(20)
r.right.left = TreeNode(15)
r.right.right = TreeNode(7)

s = Solution()
s.verticalOrder(r)