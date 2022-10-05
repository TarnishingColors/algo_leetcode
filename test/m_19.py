from structures import ListNode
from leetcode.m_19 import Solution


s = Solution()


def test_case1():
    last = ListNode(5)

    for i in range(4):
        new_node = ListNode(4 - i, last)
        last = new_node

    head = last
    res = []
    cur = s.removeNthFromEnd(head, 1)

    while cur is not None:
        res.append(cur.val)
        cur = cur.next

    assert res == [1, 2, 3, 4]


def test_case2():
    head = ListNode(1)

    cur = s.removeNthFromEnd(head, 1)

    res = []

    while cur is not None:
        res.append(cur.val)
        cur = cur.next

    assert res == []


if __name__ == "__main__":
    test_case1()
    test_case2()
