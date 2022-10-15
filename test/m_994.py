from leetcode.m_994 import Solution


s = Solution()


def test_case1():
    assert s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4


def test_case2():
    assert s.orangesRotting([[0, 2]]) == 0


def test_case3():
    assert s.orangesRotting([[0, 0, 1]]) == -1


if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()
