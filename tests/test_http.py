import math
import ipytest
from hypothesis import given
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hypothesis_cfg")),
)

from hypothesis_cfg import cfg  # type: ignore


@given(cfg("tests/cfgs/http.cfg", max_depth=50))
def test_sum(http: str):
    print(http)
    assert http != http

ipytest.run("-s")
