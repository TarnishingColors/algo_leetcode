from leetcode.e_70 import Solution


s = Solution()


def test(func):
    def inner(*args, **kwargs):
        result, expected_result = func(*args, **kwargs)

        assert result == expected_result

    return inner


@test
def test_case1():
    return s.climbStairs(2), 2


@test
def test_case2():
    return s.climbStairs(3), 3


if __name__ == "__main__":
    test_case1()
    test_case2
