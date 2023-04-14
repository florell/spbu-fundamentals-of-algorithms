from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from collections.abc import Iterable

import networkx as nx
import yaml

from src.plotting import plot_tree


@dataclass
class Node:

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################

    pass


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None

    def empty(self) -> bool:
        return self.root is None

    def to_networkx(self) -> nx.DiGraph:
        g = nx.DiGraph()

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        pass


def add_children(n: Node, nodes_info: list[Any]) -> None:

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################

    pass


if __name__ == "__main__":
    # Let's instantiate a binary tree and then implement its traversal
    # First, implement add_children() as a recursive function filling
    # in a binary tree from a tree-like dictionary (that's what is called
    # case in the code below)
    # Second, implement BinaryTree.to_networkx() as an iterative function
    # converting BinaryTree to nx.DiGraph for plotting

    with open("practicum_6/binary_tree_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for case in cases:
        bt = BinaryTree()
        if case is None:
            print("Binary tree is empty")
            continue
        key = next(iter(case.keys()))
        bt.root = Node(key=key)
        add_children(bt.root, case[key])
        plot_tree(bt.to_networkx())
        print()
