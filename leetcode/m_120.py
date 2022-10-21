from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cur_res = triangle[0][0]
        result = [cur_res]
        for row in triangle[1:]:
            cur_row_res = []
            for i in range(len(row)):
                if i == 0:
                    cur_el_res = result[0] + row[i]
                elif i == len(row) - 1:
                    cur_el_res = result[-1] + row[i]
                else:
                    cur_el_res = min(result[i - 1], result[i]) + row[i]
                cur_row_res.append(cur_el_res)
            result = cur_row_res

        return min(result)

