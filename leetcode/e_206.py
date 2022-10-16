from typing import Optional
from structures import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None

        while current:
            next_list = current.next

            current.next = previous

            previous = current
            current = next_list

        return previous
