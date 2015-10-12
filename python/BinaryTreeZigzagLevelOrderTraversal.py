__author__ = 'yihan'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        level = 1
        stack, item = [], []
        item.append(root.val)
        res.append(item)
        stack.append(root)
        while stack:
            newStack, newitem = [], []
            while stack:
                top = stack.pop(-1)
                if level % 2 == 0:
                    if top.left:
                        newStack.append(top.left)
                        newitem.append(top.left.val)
                    if top.right:
                        newStack.append(top.right)
                        newitem.append(top.right.val)
                else:
                    if top.right:
                        newStack.append(top.right)
                        newitem.append(top.right.val)
                    if top.left:
                        newStack.append(top.left)
                        newitem.append(top.left.val)
            if newitem:
                res.append(newitem)
            stack = newStack
            level += 1
        return res