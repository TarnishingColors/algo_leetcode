from leetcode.m_34 import Solution
from test.e_70 import test


s = Solution()


@test
def test_case1():
    return s.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4]


@test
def test_case2():
    return s.searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1]


@test
def test_case3():
    return s.searchRange([2, 2], 2), [0, 1]


@test
def test_case4():
    return s.searchRange([1, 3], 1), [0, 0]


if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()
    test_case4()
