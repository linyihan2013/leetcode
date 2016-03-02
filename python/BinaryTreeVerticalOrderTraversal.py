# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root: return res
        Map = collections.defaultdict(list)
        queue = []
        colQue = []
        queue.append(root)
        colQue.append(0)
        Map[0].append(root.val)
        Min, Max = 0, 0

        while queue:
            cur = queue.pop(0)
            col = colQue.pop(0)
            if cur.left:
                queue.append(cur.left)
                colQue.append(col - 1)
                Map[col - 1].append(cur.left.val)
                if col - 1 < Min: Min = col - 1
            if cur.right:
                queue.append(cur.right)
                colQue.append(col + 1)
                Map[col + 1].append(cur.right.val)
                if col + 1 > Max: Max = col + 1
        for k in range(Min, Max + 1):
            if k in Map:
                res.append(Map[k])
        return res