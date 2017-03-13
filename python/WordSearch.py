class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word: return False
        height, width = len(board), len(board[0])
        dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
        visited = [[False] * width for i in range(height)]

        def judge(word, y, x):
            if len(word) == 0: return True

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx] and word[0] == board[ny][nx]:
                    visited[ny][nx] = True
                    if judge(word[1:], ny, nx): return True
                    visited[ny][nx] = False
            return False

        for y in range(height):
            for x in range(width):
                if board[y][x] == word[0]:
                    visited[y][x] = True
                    if judge(word[1:], y, x):
                        return True
                    visited[y][x] = False
        return False