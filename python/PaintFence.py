class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0: return 0
        if n == 1: return k
        dp = [[[0, 0] for _ in range(k)] for __ in range(2)]
        for j in range(k):
            dp[0][j][0] = 1
            dp[0][j][1] = 0
        for i in range(1, n):
            Sum = 0
            for j in range(k):
                Sum += (dp[(i - 1) % 2][j][0] + dp[(i - 1) % 2][j][1])
            for j in range(k):
                dp[i % 2][j][1] = dp[(i - 1) % 2][j][0]
                dp[i % 2][j][0] = Sum - dp[(i - 1) % 2][j][0] - dp[(i - 1) % 2][j][1]
        res = 0
        for i in range(k):
            res += (dp[(n - 1) % 2][i][0] + dp[(n - 1) % 2][i][1])
        return res