from __future__ import annotations
from dataclasses import dataclass
from typing import Any

import yaml


@dataclass
class Element:
    key: Any
    data: Any = None
    np: int = None

    def next(self) -> Element:

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        pass

    def prev(self) -> Element:

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        pass


class XorDoublyLinkedList:
    def __init__(self) -> None:
        self.head: Element = None

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        pass

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        node_keys = []

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        return " <-> ".join(node_keys)

    def to_pylist(self) -> list[Any]:
        py_list = []
        next_el: Element = self.head()
        while next_el is not None:
            py_list.append(next_el.key)
            next_el = next_el.next()
        return py_list

    def empty(self):
        return self.head is None

    def search(self, k: Element) -> Element:
        """Complexity: O(n)"""

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        pass

    def insert(self, x: Element) -> None:
        """Insert to the front of the list (i.e., it is 'prepend')
        Complexity: O(1)
        """
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        pass

    def remove(self, x: Element) -> None:
        """Remove x from the list
        Complexity: O(1)
        """

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        pass

    def reverse(self) -> XorDoublyLinkedList:
        """Returns the same list but in the reserved order
        Complexity: O(1)
        """

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        pass


if __name__ == "__main__":
    # You need to implement a doubly linked list using only one pointer
    # self.np per element. In python, by pointer, we understand id(object).
    # Any object can be accessed via its id, e.g.
    # >>> import ctypes
    # >>> a = ...
    # >>> ctypes.cast(id(a), ctypes.py_object).value
    # Hint: assuming that self.next and self.prev store pointers
    # define self.np as self.np = self.next XOR self.prev

    with open("practicum_6/homework/xor_list_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        l = XorDoublyLinkedList()
        for el in reversed(c["input"]["list"]):
            l.insert(el)
        for op_info in c["input"]["ops"]:
            if op_info["op"] == "insert":
                l.remove(op_info["key"])
            elif op_info["op"] == "remove":
                l.remove(op_info["key"])
            elif op_info["op"] == "reverse":
                l = l.reverse()
        py_list = l.to_pylist()
        print(f"Case #{i + 1}: {py_list == c['output']}")
