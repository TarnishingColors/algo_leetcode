from structures import ListNode
from leetcode.e_21 import Solution


s = Solution()


def test_case1():

    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(4)

    list2 = ListNode(1)
    list2.next = ListNode(2)
    list2.next.next = ListNode(4)

    head = s.mergeTwoLists(list1, list2)

    result = []

    while head is not None:
        result.append(head.val)
        head = head.next

    assert result == [1, 1, 2, 3, 4, 4]


def test_case2():
    list1 = None

    list2 = ListNode(0)

    head = s.mergeTwoLists(list1, list2)

    res = []

    while head is not None:
        res.append(head.val)
        head = head.next

    assert res == [0]


if __name__ == "__main__":
    test_case1()
    test_case2()
