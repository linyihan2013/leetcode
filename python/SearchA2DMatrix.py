__author__ = 'yihan'
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None:
            return False
        x, y = 0, 0
        rows = len(matrix)
        columns = len(matrix[0])
        while x < rows and y < columns:
            if target < matrix[x][y]:
                return False
            elif matrix[x][y] == target:
                return True
            elif x < rows - 1 and target >= matrix[x + 1][y]:
                x += 1
            else:
                y += 1
        return False