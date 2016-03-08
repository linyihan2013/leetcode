# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.right: return self.leftmost(p.right)
        Suc = None
        while root:
            if root.val > p.val:
                Suc = root
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                break
        return Suc

    def leftmost(self, node):
        while node.left: node = node.left
        return node