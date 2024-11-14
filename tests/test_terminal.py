import ipytest
from hypothesis import given
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hypothesis_cfg")),
)

from hypothesis_cfg import cfg  # type: ignore


@given(cfg("tests/cfgs/terminal.cfg"))
def test_sum(mathexpr: str):
    assert isinstance(mathexpr, str)


ipytest.run("-s")
