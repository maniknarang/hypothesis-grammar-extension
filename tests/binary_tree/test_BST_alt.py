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
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def add_left_child(self, child):
        self.left = child

    def add_right_child(self, child):
        self.right = child

    def __repr__(self) -> str:
        return f"BSTNode({self.value}, {self.left}, {self.right})"


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
    if value < self.value and self.left and self.left.search(value):
        return True
    if value > self.value and self.right and self.right.search(value):
        return True
    return False


BSTNode.left_right_preorder = left_right_preorder  # type: ignore
BSTNode.right_left_postorder = right_left_postorder  # type: ignore
BSTNode.search = search  # type: ignore


def process_bst_str(bst_str: str) -> BSTNode:
    # print(bst_str)
    exec(bst_str, globals())  # define root: the root node of the BST
    root_node = globals()["root"]
    print(root_node)
    return root_node


"CFG VERSION"


# reversing the left-right preorder traversal should be equal to the right-left postorder traversal
@given(cfg("tests/binary_tree/cfgs/bst_alt.cfg", 10))
def test_preorder_postorder(bst_str: str):
    root = process_bst_str(bst_str)
    assert root.left_right_preorder()[::-1] == root.right_left_postorder()  # type: ignore


# BST invariant holds
@given(cfg("tests/binary_tree/cfgs/bst_alt.cfg", 10))
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
@given(cfg("tests/binary_tree/cfgs/bst_alt.cfg", 10), integers(-200, 200))
def test_search(bst_str: str, target: int):
    root = process_bst_str(bst_str)
    assert root.search(target) == (target in root.left_right_preorder())  # type: ignore


"REGEX VERSION"


# reversing the left-right preorder traversal should be equal to the right-left postorder traversal
@given(
    from_regex(
        r"""import random
node_stack = \[\]
lower_bound_stack = \[ -100 \]
upper_bound_stack = \[100\]
def left_child\(LowerBound, node_value, parent_node\):
	node_value = random\.randint\(LowerBound, node_value\)
	new_node = BSTNode\(node_value\)
	parent_node\.add_left_child\(new_node\)
	return new_node
def right_child\(node_value, UpperBound, parent_node\):
	node_value = random\.randint\(node_value, UpperBound\)
	new_node = BSTNode\(node_value\)
	parent_node\.add_right_child\(new_node\)
	return new_node
node_value = random\.randint\(lower_bound_stack\[-1\], upper_bound_stack\[-1\]\)
node = BSTNode\(node_value\)
node_stack\.append\(node\)

(
lower_bound_stack\.append\(lower_bound_stack\[-1\]\)
upper_bound_stack\.append\(node_stack\[-1\]\.value\)
node = left_child\(lower_bound_stack\[-1\], upper_bound_stack\[-1\], node_stack\[-1\]\)
node_stack\.append\(node\)
node_stack\.pop\(\)
lower_bound_stack\.pop\(\)
upper_bound_stack\.pop\(\)
)?

(
lower_bound_stack\.append\(node_stack\[-1\]\.value\)
upper_bound_stack\.append\(upper_bound_stack\[-1\]\)
node = right_child\(lower_bound_stack\[-1\], upper_bound_stack\[-1\], node_stack\[-1\]\)
node_stack\.append\(node\)
node_stack\.pop\(\)
lower_bound_stack\.pop\(\)
upper_bound_stack\.pop\(\)
)?

root = node_stack\[-1\]
""",
        fullmatch=True,
    )
)
def test_preorder_postorder_regex(bst_str: str):
    root = process_bst_str(bst_str)
    assert root.left_right_preorder()[::-1] == root.right_left_postorder()  # type: ignore


# BST invariant holds
@given(
    from_regex(
        r"""import random
node_stack = \[\]
lower_bound_stack = \[ -100 \]
upper_bound_stack = \[100\]
def left_child\(LowerBound, node_value, parent_node\):
	node_value = random\.randint\(LowerBound, node_value\)
	new_node = BSTNode\(node_value\)
	parent_node\.add_left_child\(new_node\)
	return new_node
def right_child\(node_value, UpperBound, parent_node\):
	node_value = random\.randint\(node_value, UpperBound\)
	new_node = BSTNode\(node_value\)
	parent_node\.add_right_child\(new_node\)
	return new_node
node_value = random\.randint\(lower_bound_stack\[-1\], upper_bound_stack\[-1\]\)
node = BSTNode\(node_value\)
node_stack\.append\(node\)

(
lower_bound_stack\.append\(lower_bound_stack\[-1\]\)
upper_bound_stack\.append\(node_stack\[-1\]\.value\)
node = left_child\(lower_bound_stack\[-1\], upper_bound_stack\[-1\], node_stack\[-1\]\)
node_stack\.append\(node\)
node_stack\.pop\(\)
lower_bound_stack\.pop\(\)
upper_bound_stack\.pop\(\)
)?

(
lower_bound_stack\.append\(node_stack\[-1\]\.value\)
upper_bound_stack\.append\(upper_bound_stack\[-1\]\)
node = right_child\(lower_bound_stack\[-1\], upper_bound_stack\[-1\], node_stack\[-1\]\)
node_stack\.append\(node\)
node_stack\.pop\(\)
lower_bound_stack\.pop\(\)
upper_bound_stack\.pop\(\)
)?

root = node_stack\[-1\]
""",
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
        r"""import random
node_stack = \[\]
lower_bound_stack = \[ -100 \]
upper_bound_stack = \[100\]
def left_child\(LowerBound, node_value, parent_node\):
	node_value = random\.randint\(LowerBound, node_value\)
	new_node = BSTNode\(node_value\)
	parent_node\.add_left_child\(new_node\)
	return new_node
def right_child\(node_value, UpperBound, parent_node\):
	node_value = random\.randint\(node_value, UpperBound\)
	new_node = BSTNode\(node_value\)
	parent_node\.add_right_child\(new_node\)
	return new_node
node_value = random\.randint\(lower_bound_stack\[-1\], upper_bound_stack\[-1\]\)
node = BSTNode\(node_value\)
node_stack\.append\(node\)

(
lower_bound_stack\.append\(lower_bound_stack\[-1\]\)
upper_bound_stack\.append\(node_stack\[-1\]\.value\)
node = left_child\(lower_bound_stack\[-1\], upper_bound_stack\[-1\], node_stack\[-1\]\)
node_stack\.append\(node\)
node_stack\.pop\(\)
lower_bound_stack\.pop\(\)
upper_bound_stack\.pop\(\)
)?

(
lower_bound_stack\.append\(node_stack\[-1\]\.value\)
upper_bound_stack\.append\(upper_bound_stack\[-1\]\)
node = right_child\(lower_bound_stack\[-1\], upper_bound_stack\[-1\], node_stack\[-1\]\)
node_stack\.append\(node\)
node_stack\.pop\(\)
lower_bound_stack\.pop\(\)
upper_bound_stack\.pop\(\)
)?

root = node_stack\[-1\]
""",
        fullmatch=True,
    ),
    integers(-200, 200),
)
def test_search_regex(bst_str: str, target: int):
    root = process_bst_str(bst_str)
    assert root.search(target) == (target in root.left_right_preorder())  # type: ignore


ipytest.run("-s")
