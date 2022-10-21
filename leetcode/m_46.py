from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        copy_nums = nums.copy()
        len_nums = len(nums)
        result = []

        def permutation(current_pos, cur_nums):
            if current_pos == len_nums - 1:
                result.append(cur_nums.copy())
            else:
                for i in range(current_pos, len_nums):
                    cur_nums[current_pos], cur_nums[i] = cur_nums[i], cur_nums[current_pos]
                    permutation(current_pos + 1, cur_nums.copy())

        permutation(0, copy_nums)

        return result




