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
        def code(root):
            if not root:
                vals.append('#')
                return
            vals.append(str(root.val))
            code(root.left)
            code(root.right)

        vals = []
        code(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def decode(vals):
            val = vals.pop(0) if vals else '#'
            if val == '#':
                return
            root = TreeNode(val)
            root.left = decode(vals)
            root.right = decode(vals)
            return root
        vals = data.split()
        return decode(vals)




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
