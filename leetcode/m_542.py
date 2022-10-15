from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        length = len(mat)
        width = len(mat[0])

        queue = deque()

        steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(length):
            for j in range(width):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = 20000  # because m,n <= 10^4

        while queue:
            x, y = queue.popleft()
            for dx, dy in steps:
                x_cur = dx + x
                y_cur = dy + y
                if 0 <= x_cur < length and 0 <= y_cur < width and mat[x][y] + 1 < mat[x_cur][y_cur]:
                    mat[x_cur][y_cur] = mat[x][y] + 1
                    queue.append((x_cur, y_cur))

        return mat
