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


def process_bst_str(bst_str: str) -> Node:
    exec(bst_str, globals())  # define root: the root node of the BST
    return globals()["root"]


# reversing the left-right preorder traversal should be equal to the right-left postorder traversal
@given(cfg("tests/cfgs/bst.cfg", 10))
def test_preorder_postorder(bst_str: str):
    root = process_bst_str(bst_str)
    assert root.left_right_preorder()[::-1] == root.right_left_postorder()


# BST invariant holds
@given(cfg("tests/cfgs/bst.cfg", 10))
def test_invariant(bst_str: str):
    root = process_bst_str(bst_str)

    def _test_invariant(bst_node: Node):
        if bst_node.left:
            assert bst_node.left.value <= bst_node.value
            _test_invariant(bst_node.left)
        if bst_node.right:
            assert bst_node.right.value >= bst_node.value
            _test_invariant(bst_node.right)

    _test_invariant(root)


ipytest.run("-s")
