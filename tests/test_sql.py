import ipytest
from hypothesis import given, settings
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hypothesis_cfg")),
)
from hypothesis_cfg import cfg  # type: ignore

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "sql")),
)
from sql import setup_db, execute_query  # type: ignore

# This is to set the DB up
setup_db()

@given(cfg("tests/cfgs/sql.cfg", max_depth=20))
def test_sql_query_execution(input: str):
    result = execute_query(input)
    assert 'Error' not in str(result), f'Query failed to execute with error {str(result)}'

ipytest.run("-s")
