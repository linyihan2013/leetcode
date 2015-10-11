__author__ = 'yihan'
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lists = []
        for i in range(rowIndex + 1):
            curr = []
            for j in range(i + 1):
                if j == i or j == 0:
                    curr.append(1)
                elif j - 1 >= 0 and j <= i - 1:
                    curr.append(lists[i - 1][j - 1] + lists[i - 1][j])
            lists.append(curr)
        return lists[rowIndex]