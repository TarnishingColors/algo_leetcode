from leetcode.m_77 import Solution


s = Solution()


def test(func):
    def inner(*args, **kwargs):
        result, expected_result = func(*args, **kwargs)

        assert result == expected_result

    return inner


@test
def test_case1():
    return s.combine(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]


@test
def test_case2():
    return s.combine(1, 1), [[1]]



@test
def test_case3():
    return s.combine(3, 3), [[1, 2, 3]]


if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()
