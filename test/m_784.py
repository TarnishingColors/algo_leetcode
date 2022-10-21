from leetcode.m_784 import Solution
from test.m_46 import test


s = Solution()


@test
def test_case1():
    return s.letterCasePermutation('a1b2'), ['a1b2', 'a1B2', 'A1b2', 'A1B2']


@test
def test_case2():
    return s.letterCasePermutation('c'), ['c', 'C']


if __name__ == "__main__":
    test_case1()
