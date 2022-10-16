from structures import ListNode
from leetcode.e_206 import Solution


s = Solution()


def test(func):
    def inner(*args, **kwargs):
        head, expected_result = func(*args, **kwargs)

        result_head = s.reverseList(head)
        result = []

        while result_head is not None:
            result.append(result_head.val)
            result_head = result_head.next

        assert result == expected_result

    return inner


@test
def test_case1():
    list_node = ListNode(1)
    list_node.next = ListNode(2)
    list_node.next.next = ListNode(3)
    list_node.next.next.next = ListNode(4)
    list_node.next.next.next.next = ListNode(5)

    return list_node, [5, 4, 3, 2, 1]


@test
def test_case2():
    return None, []


@test
def test_case3():
    list_node = ListNode(1)
    list_node.next = ListNode(2)

    return list_node, [2, 1]


if __name__ == "__main__":
    test_case3()
    test_case1()
    test_case2()
