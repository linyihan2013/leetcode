__author__ = 'yihan'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def findRoot(left, right, root):
            if left == right:
                return TreeNode(inorder[left])
            elif left > right:
                return None
            i = left
            for i in range(left, right + 1):
                if inorder[i] == preorder[root]:
                    break
            node = TreeNode(preorder[root])
            node.left = findRoot(left, i - 1, root + 1)
            node.right = findRoot(i + 1, right, root + i - left + 1)
            return node
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        return findRoot(0, len(preorder) - 1, 0)