from leetcode.m_46 import Solution


s = Solution()


def test(func):
    def inner(*args, **kwargs):
        result, expected_result = func(*args, **kwargs)

        assert [x in expected_result for x in result] and [x in result for x in expected_result]

    return inner


@test
def test_case1():
    return s.permute([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


if __name__ == "__main__":
    test_case1()
