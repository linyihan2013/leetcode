__author__ = 'yihan'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(1, n)

    def helper(self, left, right):
        res = []
        if left > right:
            res.append(None)
            return res
        for i in range(left, right + 1):
            leftlist = self.helper(left, i - 1)
            rightlist = self.helper(i + 1, right)
            for j in range(0, len(leftlist)):
                for k in range(0, len(rightlist)):
                    root = TreeNode(i)
                    root.left = leftlist[j]
                    root.right = rightlist[k]
                    res.append(root)
        return res