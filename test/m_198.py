from leetcode.m_198 import Solution
from test.e_70 import test


s = Solution()


@test
def test_case1():
    return s.rob([2, 7, 9, 3, 1]), 12


if __name__ == "__main__":
    test_case1()
