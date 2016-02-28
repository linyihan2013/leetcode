class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        h = len(matrix)
        if h == 0: return 0
        w = len(matrix[0])
        dp = [[0] * w for x in range(h)]

        def dfs(x, y):
            for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] > matrix[x][y]:
                    if not dp[nx][ny]: dp[nx][ny] = dfs(nx, ny)
                    dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
                dp[x][y] = max(dp[x][y], 1)
            return dp[x][y]

        for x in range(h):
            for y in range(w):
                if not dp[x][y]: dp[x][y] = dfs(x, y)
        return max([max(x) for x in dp])