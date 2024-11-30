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
    def __init__(self, value: int, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.value}, {self.left}, {self.right})"

    def add_left_child(self, child):
        self.left = child

    def add_right_child(self, child):
        self.right = child

    def left_right_preorder(self):
        return (
            [self.value]
            + (self.left.left_right_preorder() if self.left else [])
            + (self.right.left_right_preorder() if self.right else [])
        )

    def right_left_postorder(self):
        return (
            (self.right.right_left_postorder() if self.right else [])
            + (self.left.right_left_postorder() if self.left else [])
            + [self.value]
        )

    def search(self, value: int) -> bool:
        if self.value == value:
            return True
        if self.left and self.left.search(value):
            return True
        if self.right and self.right.search(value):
            return True
        return False


def process_bt_str(bst_str: str) -> Node:
    return eval(bst_str, globals())  # define root: the root node of the BT


# reversing the left-right preorder traversal should be equal to the right-left postorder traversal
@given(cfg("tests/cfgs/bt.cfg", 10))
def test_preorder_postorder(bt_str: str):
    root = process_bt_str(bt_str)
    assert root.left_right_preorder()[::-1] == root.right_left_postorder()


# "more efficient" search is still correct
@given(cfg("tests/cfgs/bt.cfg", 10))
def test_search(bt_str: str):
    root = process_bt_str(bt_str)
    target = random.randint(-200, 200)
    assert root.search(target) == (target in root.left_right_preorder())


ipytest.run("-s")
