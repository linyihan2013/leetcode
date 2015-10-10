__author__ = 'yihan'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        result += self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result.append(root.val)
        return result