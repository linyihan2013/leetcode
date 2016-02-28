# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.isSubtreeLessThan(root.left, root.val) and self.isSubtreeGreaterThan(root.right, root.val) and self.isValidBST(root.left) and self.isValidBST(root.right)

    def isSubtreeLessThan(self, node, val):
        if not node: return True
        return node.val < val and self.isSubtreeLessThan(node.left, val) and self.isSubtreeLessThan(node.right, val)

    def isSubtreeGreaterThan(self, node, val):
        if not node: return True
        return node.val > val and self.isSubtreeGreaterThan(node.left, val) and self.isSubtreeGreaterThan(node.right, val)