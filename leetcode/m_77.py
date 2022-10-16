from typing import List
from collections import deque


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        all_values = [x for x in range(1, n + 1)]
        result = []
        queue = deque()

        for x in range(1, n + 1):
            queue.append([[x], all_values[x:], k - 1])

        while queue:
            res, nums, steps_left = queue.popleft()

            if steps_left != 0:
                for i in range(len(nums)):
                    cur_res = res + [nums[i]]
                    if len(cur_res):
                        queue.append([cur_res, nums[i + 1:], steps_left - 1])

            else:
                result.append(res)

        return result


