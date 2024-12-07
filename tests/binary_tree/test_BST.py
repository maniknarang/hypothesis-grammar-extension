from logging import root
import math
import ipytest
from hypothesis import given
from hypothesis.strategies import integers, from_regex
import sys
import os
import random

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "hypothesis_cfg")),
)

from hypothesis_cfg import cfg  # type: ignore


class BSTNode:
    def __init__(self, left, right):
        self.value = None
        self.left = left
        self.right = right

    def initialize_value(self, lower_bound, upper_bound):
        self.value = random.randint(lower_bound, upper_bound)
        if self.left:
            self.left.initialize_value(lower_bound, self.value)
        if self.right:
            self.right.initialize_value(self.value, upper_bound)
        return self

    def __repr__(self) -> str:
        return f"BSTNode({self.value}, {self.left}, {self.right})"


def left_right_preorder(self):
    left = []
    right = []
    if self.left:
        left = self.left.left_right_preorder()
    if self.right:
        right = self.right.left_right_preorder()
    return [self.value] + left + right


def right_left_postorder(self):
    right = []
    left = []
    if self.right:
        right = self.right.right_left_postorder()
    if self.left:
        left = self.left.right_left_postorder()
    return right + left + [self.value]


def search(self, value: int) -> bool:
    if self.value == value:
        return True
    if value < self.value and self.left and self.left.search(value):  # type: ignore
        return True
    if value > self.value and self.right and self.right.search(value):  # type: ignore
        return True
    return False


BSTNode.left_right_preorder = left_right_preorder  # type: ignore
BSTNode.right_left_postorder = right_left_postorder  # type: ignore
BSTNode.search = search  # type: ignore


def process_bst_str(bst_str: str) -> BSTNode:
    # print(bst_str)
    unitialized_bst_root = eval(bst_str)
    initialized_bst_root = unitialized_bst_root.initialize_value(-100, 100)
    print(initialized_bst_root)
    return initialized_bst_root


"CFG VERSION"


# reversing the left-right preorder traversal should be equal to the right-left postorder traversal
@given(cfg("tests/binary_tree/cfgs/bst.cfg", 10))
def test_preorder_postorder(bst_str: str):
    root = process_bst_str(bst_str)
    assert root.left_right_preorder()[::-1] == root.right_left_postorder()  # type: ignore


# BST invariant holds
@given(cfg("tests/binary_tree/cfgs/bst.cfg", 10))
def test_invariant(bst_str: str):
    root = process_bst_str(bst_str)

    def _test_invariant(bst_node: BSTNode):
        if bst_node.left:
            assert bst_node.left.value <= bst_node.value
            _test_invariant(bst_node.left)
        if bst_node.right:
            assert bst_node.right.value >= bst_node.value
            _test_invariant(bst_node.right)

    _test_invariant(root)


# BST O(log n) search is correct
@given(cfg("tests/binary_tree/cfgs/bst.cfg", 10), integers(-200, 200))
def test_search(bst_str: str, target: int):
    root = process_bst_str(bst_str)
    assert root.search(target) == (target in root.left_right_preorder())  # type: ignore


"REGEX VERSION"


# reversing the left-right preorder traversal should be equal to the right-left postorder traversal
@given(
    from_regex(
        r"BSTNode\( ((None)|(BSTNode\( None, None \))) , ((None)|(BSTNode\( None, None \))) \)",
        fullmatch=True,
    )
)
def test_preorder_postorder_regex(bst_str: str):
    root = process_bst_str(bst_str)
    assert root.left_right_preorder()[::-1] == root.right_left_postorder()  # type: ignore


# BST invariant holds
@given(
    from_regex(
        r"BSTNode\( ((None)|(BSTNode\( None, None \))) , ((None)|(BSTNode\( None, None \))) \)",
        fullmatch=True,
    )
)
def test_invariant_regex(bst_str: str):
    root = process_bst_str(bst_str)

    def _test_invariant(bst_node: BSTNode):
        if bst_node.left:
            assert bst_node.left.value <= bst_node.value
            _test_invariant(bst_node.left)
        if bst_node.right:
            assert bst_node.right.value >= bst_node.value
            _test_invariant(bst_node.right)

    _test_invariant(root)


# BST O(log n) search is correct
@given(
    from_regex(
        r"BSTNode\( ((None)|(BSTNode\( None, None \))) , ((None)|(BSTNode\( None, None \))) \)",
        fullmatch=True,
    ),
    integers(-200, 200),
)
def test_search_regex(bst_str: str, target: int):
    root = process_bst_str(bst_str)
    assert root.search(target) == (target in root.left_right_preorder())  # type: ignore


ipytest.run("-s")
