from __future__ import annotations
from dataclasses import dataclass
from typing import Any
import ctypes
import yaml


@dataclass
class Element:
    key: Any
    data: Any = None
    np: int = 0
    index: int = -1

    def next(self, prev_p):
        return self.np ^ prev_p

    def prev(self,next_p):
        return self.np ^ next_p


class XorDoublyLinkedList:
    def __init__(self) -> None:
        self.head: Element = None
        self.tail: Element = None
        self.nodes = []
        self.key_to_index = {}


    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        node_keys = []
        next_p = id(self.head)
        prev_p = 0
        while next_p != 0:
            next_el = ctypes.cast(next_p, ctypes.py_object).value
            node_keys.append(str(next_el.key))
            prev_p, next_p = next_p, next_el.next(prev_p)
        return " <-> ".join(node_keys)

    def to_pylist(self) -> list[Any]:
        py_list = []
        next_p = id(self.head)
        prev_p = 0
        while next_p != 0:
            next_el = ctypes.cast(next_p, ctypes.py_object).value
            py_list.append(next_el.key)
            prev_p, next_p = next_p, next_el.next(prev_p)
        return py_list

    def empty(self):
        return self.head is None

    def search(self, k: Element) -> Element:
        """Complexity: O(n)"""
        next_p = id(self.head)
        prev_p = 0
        while next_p != 0 and next_el.key != k.key:
            next_el = ctypes.cast(next_p, ctypes.py_object).value
            prev_p, next_p = next_p, next_el.next(prev_p)
        return next_el

    def insert(self, x: Element) -> None:
        """Insert to the front of the list (i.e., it is 'prepend')
        Complexity: O(1)
        """
        if self.head is None:
            x.index = 0
            self.head = x
            self.tail = x
        else:
            x.index = self.head.index + 1
            self.head.np = id(x) ^ self.head.np
            x.np = id(self.head)
            self.head = x
            for node in self.nodes:
                if node.index >= x.index:
                    node.index += 1
        self.nodes.append(x)

    def remove(self, x: Element) -> None:
        """Remove x from the list
        Complexity: O(1)
        """
        if x.index == -1:
            return

        index = self.key_to_index.get(x.key)
        if index is None:
            return

        del self.key_to_index[x.key]
        if len(self.nodes) == 1:
            self.head = None
            self.tail = None
        elif x is self.head:
            self.head = ctypes.cast(x.next(0), ctypes.py_object).value
            self.head.np = self.head.np ^ id(x)
            self.head.index = 0
        elif x is self.tail:
            self.tail = ctypes.cast(x.prev(0), ctypes.py_object).value
            self.tail.np = self.tail.np ^ id(x)
            self.tail.index = len(self.nodes) - 2
        else:
            prev_p = x.prev(0)
            next_p = x.next(prev_p)
            prev_el = ctypes.cast(prev_p, ctypes.py_object).value
            next_el = ctypes.cast(next_p, ctypes.py_object).value
            prev_el.np = prev_el.np ^ id(x) ^ next_p
            next_el.np = next_el.np ^ id(x) ^ prev_p
            for i in range(index + 1, len(self.nodes)):
                self.nodes[i].index -= 1
        self.nodes.pop(index)
        x.index = -1

    def reverse(self) -> XorDoublyLinkedList:
        """Returns the same list but in the reserved order
        Complexity: O(1)
        """
        self.head, self.tail = self.tail, self.head
        return self

if __name__ == "__main__":
    # You need to implement a doubly linked list using only one pointer
    # self.np per element. In python, by pointer, we understand id(object).
    # Any object can be accessed via its id, e.g.
    # >>> import ctypes
    # >>> a = ...
    # >>> ctypes.cast(id(a), ctypes.py_object).value
    # Hint: assuming that self.next and self.prev store pointers
    # define self.np as self.np = self.next XOR self.prev

    with open("xor_list_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        l = XorDoublyLinkedList()
        for el in reversed(c["input"]["list"]):
            l.insert(Element(key=el))
        for op_info in c["input"]["ops"]:
            if op_info["op"] == "insert":
                l.insert(Element(key=op_info["key"]))
            elif op_info["op"] == "remove":
                l.remove(Element(key=op_info["key"]))
            elif op_info["op"] == "reverse":
                l = l.reverse()
        py_list = l.to_pylist()
        print(py_list)
        print(f"Case #{i + 1}: {py_list == c['output']}")
