from __future__ import annotations


class TreeNode:
    def __init__(self, val: int):
        self.val = val

    val: int
    left: TreeNode = None
    right: TreeNode = None


def is_tree_symmetric(node: TreeNode) -> bool:
    return True if node is None else is_tree_symmetric_helper(node.left, node.right)


def is_tree_symmetric_helper(left: TreeNode, right: TreeNode) -> bool:
    if left is None and right is None:
        return True
    elif left is not None and right is None:
        return False
    elif left is None and right is not None:
        return False
    else:
        return (
            left.val == right.val
            and is_tree_symmetric_helper(left.right, right.left)
            and is_tree_symmetric_helper(left.left, right.right)
        )


# Level 1
one = TreeNode(1)
# Level 2
two, three = TreeNode(2), TreeNode(2)
# Level 3
four, five, six, seven = TreeNode(3), TreeNode(4), TreeNode(4), TreeNode(3)

one.left, one.right = two, three
two.left, two.right = four, five
three.left, three.right = six, seven

assert is_tree_symmetric(one) is True
