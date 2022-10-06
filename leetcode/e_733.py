from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = [[sr, sc]]
        m = len(image)
        n = len(image[0])

        def actual_fill(sr: int, sc: int):
            if sr != 0 and [sr - 1, sc] not in seen:
                if image[sr - 1][sc] == image[sr][sc]:
                    seen.append([sr - 1, sc])
                    actual_fill(sr - 1, sc)
            if sr < m - 1 and [sr + 1, sc] not in seen:
                if image[sr + 1][sc] == image[sr][sc]:
                    seen.append([sr + 1, sc])
                    actual_fill(sr + 1, sc)
            if sc != 0 and [sr, sc - 1] not in seen:
                if image[sr][sc - 1] == image[sr][sc]:
                    seen.append([sr, sc - 1])
                    actual_fill(sr, sc - 1)
            if sc < n - 1 and [sr, sc + 1] not in seen:
                if image[sr][sc + 1] == image[sr][sc]:
                    seen.append([sr, sc + 1])
                    actual_fill(sr, sc + 1)

        actual_fill(sr, sc)

        for i in range(len(seen)):
            image[seen[i][0]][seen[i][1]] = color

        return image
