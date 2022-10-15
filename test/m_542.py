from leetcode.m_542 import Solution


s = Solution()


def test_case1():
    assert s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]


def test_case2():
    assert s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]


if __name__ == "__main__":
    test_case1()
    test_case2()
