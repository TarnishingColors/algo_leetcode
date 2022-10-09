from structures import TreeNode

from leetcode.e_617 import Solution


s = Solution()


def test_case1():
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(7)

    result = []
    stack = [s.mergeTrees(root1, root2)]
    while stack:
        cur = stack.pop(0)
        result.append(cur.val if cur else None)
        if cur and (cur.left or cur.right):
            stack.extend([cur.left, cur.right])

    assert result == [3, 4, 5, 5, 4, None, 7]


if __name__ == "__main__":
    test_case1()
