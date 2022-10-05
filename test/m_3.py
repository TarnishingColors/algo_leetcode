from leetcode.m_3 import Solution


s = Solution()


def test_case1():
    assert s.lengthOfLongestSubstring('abcabcbb') == 3


def test_case2():
    assert s.lengthOfLongestSubstring('bbbbb') == 1


def test_case3():
    assert s.lengthOfLongestSubstring('pwwkew') == 3


if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()
