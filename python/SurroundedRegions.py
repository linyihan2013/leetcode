__author__ = 'yihan'
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def fill(x, y):
            if x < 0 or x > rows - 1 or y < 0 or y > columns - 1 or board[x][y] != 'O':
                return
            queue.append((x, y))
            board[x][y] = 'D'
        def bfs(x, y):
            fill(x, y)
            while queue:
                curr = queue.pop(0); i = curr[0]; j = curr[1]
                fill(i - 1, j); fill(i + 1, j); fill(i, j - 1); fill(i, j + 1)
        if len(board) == 0:
            return
        rows = len(board)
        columns = len(board[0])
        queue = []
        for i in range(rows):
            bfs(i, 0); bfs(i, columns - 1)
        for j in range(columns):
            bfs(0, j); bfs(rows - 1, j)
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == 'D': board[i][j] = 'O'
                elif board[i][j] == 'O': board[i][j] = 'X'
