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
        def dolt(node):
            if node:
                vals.append(str(node.val))
                dolt(node.left)
                dolt(node.right)
            else:
                vals.append('#')
        vals = []
        dolt(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dolt():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dolt()
            node.right = dolt()
            return node
        vals = iter(data.split())
        return dolt()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))