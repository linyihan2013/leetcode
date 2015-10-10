__author__ = 'yihan'
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        node = root
        while node:
            depth += 1
            node = node.left
        if depth == 0:
            return 0
        left, right = 0, (1 << (depth - 1)) - 1
        while left <= right:
            mid = (left + right) >> 1
            if self.getNode(root, mid, depth - 1):
                left = mid + 1
            else:
                right = mid - 1
        return (1 << (depth - 1)) + right

    def getNode(self, root, path, depth):
        while depth and root:
            if path & (1 << (depth - 1)):
                root = root.right
            else:
                root = root.left
            depth -= 1
        return root