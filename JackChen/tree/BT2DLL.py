class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bt2dll(root):
    def helper(root, head):
        if not root:
            return None
        helper(root.right, head)
        if head[0]:
            head[0].left = root
        root.right = head[0]
        head[0] = root
        helper(root.left, head)

    head = [None]
    helper(root, head)
    return head[0]



# Build a BST for testing purpose
bst = TreeNode(4)
bst.left = TreeNode(2)
bst.right = TreeNode(6)
bst.left.left = TreeNode(1)
bst.left.right = TreeNode(3)
bst.right.left = TreeNode(5)
bst.right.right = TreeNode(7)

"""
        4
    2       6
1      3, 5   7

-->

1,2,3,4,5,6,7
"""

head = bt2dll(bst)
while head:
    print head.val
    head = head.right