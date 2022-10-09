from typing import Optional
from structures import Node


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root

        root.next = None
        stack = []

        if root.left:
            stack = [root.left, root.right]

        while stack:
            cur = []
            cur_len = len(stack)
            for i in range(cur_len):
                cur_node = stack.pop(0)
                if i != cur_len - 1:
                    cur_node.next = stack[0]
                if cur_node.left and cur_node.right:
                    cur.extend([cur_node.left, cur_node.right])
            stack.extend(cur)
        return root
