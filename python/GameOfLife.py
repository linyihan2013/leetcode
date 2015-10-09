class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dx = (-1, 0, 1, -1, 1, -1, 0, 1)
        dy = (-1, -1, -1, 0, 0, 1, 1, 1)
        for y in range(len(board)):
            for x in range(len(board[0])):
                lives = 0
                for z in range(8):
                    nx, ny = x + dx[z], y + dy[z]
                    lives += self.check(nx, ny, board)
                if lives == 3 or lives + board[ny][nx] == 3:
                    board[ny][nx] |= 2;
        for y in range(len(board)):
            for x in range(len(board[0])):
                board[y][x] >>= 1;

    def check(self, nx, ny, board):
        if nx < 0 or ny < 0 or nx > range(len(board[0])) or ny > range(len(board)):
            return 0
        return board[ny][nx] & 1;