# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # preorder, null saved as '#'
        encoded, stack = [], [root]
        while stack:
            node = stack.pop()
            if not node:
                encoded.append('#')
            else:
                encoded.append(node.val)
                stack.append(root.right)
                stack.append(root.left)

        return ','.join(encoded)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs(encoded):
            if not encoded:
                return
            c = encoded.pop()
            if c == '#':
                return None
            node = TreeNode(int(c))
            node.left = dfs()
            node.right = dfs()
            return node
        encoded = data.split(',')[::-1]
        return dfs()




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



# Your Codec object will be instantiated and called as such:
codec = Codec()
# codec.deserialize(codec.serialize(root))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

s = codec.serialize(root)
r = codec.deserialize(s)
print s
print r
