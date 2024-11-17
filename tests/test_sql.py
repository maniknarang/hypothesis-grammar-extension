import ipytest
from hypothesis import given
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hypothesis_cfg")),
)
from hypothesis_cfg import cfg  # type: ignore

@given(cfg("tests/cfgs/sql.cfg", max_depth=10))
def test_select(input: str):
    print(f'Generated SQL query is "{input}"')

ipytest.run("-s")
