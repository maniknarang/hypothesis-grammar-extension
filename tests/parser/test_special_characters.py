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


@given(cfg("tests/parser/cfgs/special_characters.cfg"))
def test_sum(string: str):
    assert "\\n" in string


ipytest.run("-s")
