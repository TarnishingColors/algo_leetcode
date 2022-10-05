from typing import Optional
from structures import ListNode


# https://leetcode.com/problems/remove-nth-node-from-end-of-list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fake = ListNode(0, head)
        search_n = fake
        search_n_end = fake
        for _ in range(n):
            search_n = search_n.next
        while search_n.next is not None:
            search_n = search_n.next
            search_n_end = search_n_end.next
        search_n_end.next = search_n_end.next.next
        return fake.next
