from leetcode.m_567 import Solution


s = Solution()


def test_case1():
    assert s.checkInclusion('ab', 'eidbaooo')


def test_case2():
    assert not s.checkInclusion('ab', 'eidboaoo')


def test_case3():
    assert s.checkInclusion('adc', 'dcda')


if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()
