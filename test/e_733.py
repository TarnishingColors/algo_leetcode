from leetcode.e_733 import Solution


s = Solution()


def test_case1():
    assert s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


def test_case2():
    assert s.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [[0, 0, 0], [0, 0, 0]]


if __name__ == "__main__":
    test_case1()
    test_case2()
