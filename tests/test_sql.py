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
from sql import setup_dbs, execute_query_sqlite3, execute_query_duckdb  # type: ignore

@given(cfg("tests/cfgs/sql1.cfg", max_depth=20))
def test_sql_query_syntax(input: str):
    """Property 1: test generated SQL query syntax in SQLite3 DB"""
    result = execute_query_sqlite3(input)
    assert 'Error' not in str(result), f'Query failed to execute with error {str(result)}'

@given(cfg("tests/cfgs/sql2.cfg", max_depth=20))
def test_sql_query_where_clause(input: str):
    """Property 2: test WHERE clause and verify SQLite3 and DuckDB return the same results"""
    result_sqlite3 = execute_query_sqlite3(input)
    result_duckdb = execute_query_duckdb(input)
    print('SQLite3 output:', result_sqlite3)
    print('DuckDB output:', result_duckdb)
    assert sorted(result_sqlite3) == sorted(result_duckdb)

@given(cfg("tests/cfgs/sql3.cfg", max_depth=20))
def test_sql_query_group_by_clause(input:str):
    """Property 3: test GROUP BY clause and verify SQLite3 and DuckDB return the same results"""
    result_sqlite3 = execute_query_sqlite3(input)
    result_duckdb = execute_query_duckdb(input)
    print('SQLite3 output:', result_sqlite3)
    print('DuckDB output:', result_duckdb)
    assert sorted(result_sqlite3) == sorted(result_duckdb)

ipytest.run("-s")
