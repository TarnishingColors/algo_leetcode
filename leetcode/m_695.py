from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        x_size = len(grid)
        y_size = len(grid[0])
        max_sq = 0
        neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def area_square_calc(x0: int, y0: int):
            acc_sq = 1
            for x1, y1 in neighbours:
                x, y = x0 + x1, y0 + y1
                if 0 <= x < x_size and 0 <= y < y_size and grid[x][y] and (x, y) not in visited:
                    visited.add((x, y))
                    acc_sq += area_square_calc(x, y)
            return acc_sq

        for i in range(x_size):
            for j in range(y_size):
                if grid[i][j] and (i, j) not in visited:
                    visited.add((i, j))
                    max_sq = max(area_square_calc(i, j), max_sq)

        return max_sq
