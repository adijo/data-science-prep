from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None


def is_tree_symmetric(node: TreeNode) -> bool:
    def _is_tree_symmetric(left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        elif left is not None and right is None:
            return False
        elif left is None and right is not None:
            return False
        else:
            return (
                left.val == right.val
                and _is_tree_symmetric(left.right, right.left)
                and _is_tree_symmetric(left.left, right.right)
            )

    return True if node is None else _is_tree_symmetric(node.left, node.right)


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
