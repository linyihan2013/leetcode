# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.longest(root, None, 0)

    def longest(self, now, parent, len):
        if not now: return len
        len = len + 1 if parent and now.val == parent.val + 1 else 1
        return max(len, self.longest(now.left, now, len), self.longest(now.right, now, len))