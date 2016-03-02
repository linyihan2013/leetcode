class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n, p = len(A), len(A[0]), len(B[0])
        C = [[0] * p for i in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    for k in range(p):
                        C[i][k] += A[i][j] * B[j][k]
        return C