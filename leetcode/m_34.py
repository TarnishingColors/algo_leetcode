from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def find_min_pos(low, high):
            res = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    res = mid
                    high = mid - 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return res

        def find_max_pos(low, high):
            res = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    res = mid
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return res

        lowest = find_min_pos(0, len(nums) - 1)
        highest = find_max_pos(lowest, len(nums) - 1)
        return [lowest, highest]
