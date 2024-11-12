import ipytest
from hypothesis import given
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hypothesis_cfg")),
)

from hypothesis_cfg import cfg


def sum(mathexpr: str) -> int:
    print(f"Testing mathexpr: {mathexpr}")
    return eval(mathexpr)


@given(cfg("tests/grammar.cfg"))
def test_sum(mathexpr: str):
    assert sum(mathexpr) == eval(mathexpr)


ipytest.run()
