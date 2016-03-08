class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        height = len(rooms)
        width = len(rooms[0]) if height else 0
        if height == 0: return
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        queue = []
        for i in range(height):
            for j in range(width):
                if rooms[i][j] == 0:
                    queue.append([i, j])
        while queue:
            cur = queue.pop()
            x, y = cur[0], cur[1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < height and 0 <= ny < width and rooms[nx][ny] > rooms[x][y] + 1:
                    rooms[nx][ny] = rooms[x][y] + 1
                    queue.append([nx, ny])