import math
import ipytest
from hypothesis import given
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "hypothesis_cfg")),
)

from hypothesis_cfg import cfg  # type: ignore


def sum_expr_string(mathexpr: str) -> int:
    return sum(int(num) for num in mathexpr.split("+"))


@given(cfg("tests/parser/cfgs/recursive.cfg"))
def test_sum(mathexpr: str):
    print(mathexpr)
    assert sum_expr_string(mathexpr) == eval(mathexpr)


ipytest.run("-s")
