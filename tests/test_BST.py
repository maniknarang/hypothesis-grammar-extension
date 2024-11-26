from logging import root
import math
import ipytest
from hypothesis import given
import sys
import os
import random

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hypothesis_cfg")),
)

from hypothesis_cfg import cfg  # type: ignore


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value}, {self.left}, {self.right})"

    def add_left_child(self, child):
        self.left = child

    def add_right_child(self, child):
        self.right = child


def sum_expr_string(mathexpr: str) -> int:
    return sum(int(num) for num in mathexpr.split("+"))


@given(cfg("tests/cfgs/bst.cfg", 10))
def test_sum(bst_str: str):
    exec(bst_str, globals())  # define root: the root node of the BST
    root = globals()["root"]
    print(root)


ipytest.run("-s")
