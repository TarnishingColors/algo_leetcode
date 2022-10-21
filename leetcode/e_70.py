class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (1, 0):
            return 1

        res = [0] * (n + 1)
        res[0] = res[1] = 1

        for i in range(2, len(res)):
            res[i] = res[i - 1] + res[i - 2]

        return res[-1]
