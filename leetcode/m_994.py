import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length = len(grid)
        width = len(grid[0])

        minutes = 0

        queue = collections.deque()

        fresh_oranges = []

        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(length):
            for j in range(width):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges.append((i, j))

        queue.append(minutes)

        while queue:
            el = queue.popleft()
            if type(el) is int:
                minutes = el
                if queue:
                    queue.append(minutes + 1)
            else:
                x, y = el
                for dx, dy in steps:
                    cur_x = x + dx
                    cur_y = y + dy
                    if 0 <= cur_x < length and 0 <= cur_y < width and grid[cur_x][cur_y] == 1:
                        grid[cur_x][cur_y] = 2
                        fresh_oranges.remove((cur_x, cur_y))
                        queue.append((cur_x, cur_y))

        if fresh_oranges:
            return -1

        return minutes
