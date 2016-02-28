# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    res = 0

    class Node(object):
        def __init__(self):
            self.isBST = False
            self.min = 0x7fffffff
            self.max = -0x7fffffff
            self.size = 0

    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.Helper(root)
        return self.res

    def Helper(self, root):
        cur = self.Node()
        if not root:
            cur.isBST = True
            return cur
        left = self.Helper(root.left)
        right = self.Helper(root.right)
        if left.isBST and root.val > left.max and right.isBST and root.val < right.min:
            cur.isBST = True
            cur.min = min(root.val, left.min)
            cur.max = max(root.val, right.max)
            cur.size = 1 + left.size + right.size
            if cur.size > self.res: self.res = cur.size
        return cur