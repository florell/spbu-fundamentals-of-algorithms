from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional

import yaml


@dataclass
class Element:

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################

    pass


class DoublyLinkedList:

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################

    pass


def read_from_str(s: str) -> DoublyLinkedList:
    l = DoublyLinkedList()
    for digit in list(s):
        l.insert(Element(key=int(digit)))
    return l


def add_two_numbers(l1: DoublyLinkedList, l2: DoublyLinkedList) -> DoublyLinkedList:

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################

    pass


if __name__ == "__main__":
    # Let's solve Add Two Numbers problem from leetcode.com:
    # https://leetcode.com/problems/add-two-numbers/description/

    # l = DoublyLinkedList()
    # l.insert(Element(key=1))
    # l.insert(Element(key=2))
    # l.insert(Element(key=3))
    # l.insert(Element(key=4))
    # e = l.search(Element(key=3))
    # l.remove(e)

    with open("practicum_6/add_two_numbers_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for c in cases:
        l1 = read_from_str(c["input"]["a"])
        l2 = read_from_str(c["input"]["b"])
        l_sum_true = read_from_str(c["output"])
        l_sum = add_two_numbers(l1, l2)
        print(
            f"Input: a = {c['input']['a']}, b = {c['input']['b']}. "
            f"Output: {l_sum}. "
            f"Expected output: {l_sum_true}"
        )
