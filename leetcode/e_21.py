from typing import Optional
from structures import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1:
            if list2 and list1.val > list2.val:
                head = list2
                list2 = list2.next
            else:
                head = list1
                list1 = list1.next
        elif list2:
            head = list2
            list2 = list2.next
        else:
            return None

        cur_res = head

        while list1 and list2:
            if list1.val > list2.val:
                cur_res.next = list2
                list2 = list2.next
            else:
                cur_res.next = list1
                list1 = list1.next
            cur_res = cur_res.next

        while list1:
            cur_res.next = list1
            list1 = list1.next
            cur_res = cur_res.next

        while list2:
            cur_res.next = list2
            list2 = list2.next
            cur_res = cur_res.next

        return head
