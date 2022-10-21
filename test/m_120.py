from leetcode.m_120 import Solution
from test.e_70 import test


s = Solution()


@test
def test_case1():
    return s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]), 11


if __name__ == "__main__":
    test_case1()
