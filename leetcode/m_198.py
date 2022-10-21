from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        len_nums = len(nums)
        cur_max = nums[0]
        res = [nums[0]] + [0] * (len_nums - 1)

        if len_nums > 1:
            res[1] = nums[1]
            cur_max = max(cur_max, nums[1])
            for i in range(2, len_nums):
                new_val = max(res[i - 3] if i > 2 else 0, res[i - 2]) + nums[i]
                cur_max = max(new_val, cur_max)
                res[i] = new_val
        return cur_max
