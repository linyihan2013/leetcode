__author__ = 'yihan'
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        clean_rows = set()
        clean_columns = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] is 0:
                    clean_rows.add(i)
                    clean_columns.add(j)
        for i in clean_rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in range(len(matrix)):
            for j in clean_columns:
                matrix[i][j] = 0