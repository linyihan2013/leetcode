# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.isSymmetric(root.left, root.right)

    def isSymmetric(self, lt, rt):
        if not lt and not rt: return True
        if (not lt and rt) or (lt and not rt) or (lt.val != rt.val): return False
        return self.isSymmetric(lt.left, rt.right) and self.isSymmetric(lt.right, rt.left)