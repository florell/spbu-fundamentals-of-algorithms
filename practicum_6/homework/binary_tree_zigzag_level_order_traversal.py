from __future__ import annotations
from dataclasses import dataclass
from typing import Any

import yaml


@dataclass
class Node:
    key: Any
    data: Any = None
    left: Node = None
    right: Node = None


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None

    def empty(self) -> bool:
        return self.root is None

    def zigzag_level_order_traversal(self) -> list[list[Any]]:
        result = []
        if self.empty():
            return result

        current_level = [self.root]
        zigzag = False

        while current_level:
            current_vals = []
            next_level = []

            for node in current_level:
                current_vals.append(node.key)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if zigzag:
                current_vals.reverse()

            result.append(current_vals)
            current_level = next_level
            zigzag = not zigzag

        return result


def build_tree(list_view: list[Any]) -> BinaryTree:
    bt = BinaryTree()

    if not list_view:
        return bt

    nodes = []
    for val in list_view:
        if val is None:
            nodes.append(None)
        else:
            nodes.append(Node(val))

    for i, node in enumerate(nodes):
        if node:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if left_child < len(nodes):
                node.left = nodes[left_child]
            if right_child < len(nodes):
                node.right = nodes[right_child]

    bt.root = nodes[0]
    return bt


if __name__ == "__main__":
    # Let's solve Binary Tree Zigzag Level Order Traversal problem from leetcode.com:
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    # First, implement build_tree() to read a tree from a list format to our class
    # Second, implement BinaryTree.zigzag_traversal() returning the list required by the task
    # Avoid recursive traversal!

    with open(
        "binary_tree_zigzag_level_order_traversal_cases.yaml", "r"
    ) as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        bt = build_tree(c["input"])
        zz_traversal = bt.zigzag_level_order_traversal()
        print(f"Case #{i + 1}: {zz_traversal == c['output']}")
