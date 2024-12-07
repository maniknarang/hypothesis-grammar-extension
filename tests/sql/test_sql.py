import ipytest
from hypothesis import given
import sys
import os
import unittest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "hypothesis_cfg")),
)
from hypothesis_cfg import cfg  # type: ignore

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "sql")),
)
from sql import setup_dbs, execute_query_sqlite3, execute_query_duckdb, del_dbs  # type: ignore

num_valid_queries = 0
num_total_queries = 0

class SQLTest(unittest.TestCase):
    def setUp(self):
        setup_dbs()

    @given(cfg("tests/sql/cfgs/sql1.cfg", max_depth=20))
    def test_sql_query_syntax(self, input: str):
        """Property 1: test generated SQL query syntax in SQLite3 DB"""
        print('SQL input:', input)
        global num_valid_queries
        global num_total_queries
        num_total_queries += 1

        result1 = execute_query_sqlite3(input)
        result2 = execute_query_duckdb(input)
        if "Error" not in result1 and "Error" not in result2:
            num_valid_queries += 1
        assert "Error" not in str(
            result1
        ), f"Query failed to execute with error {str(result1)}"


    @given(cfg("tests/sql/cfgs/sql2.cfg", max_depth=20))
    def test_sql_query_where_clause(self, input: str):
        """Property 2: test WHERE clause and verify SQLite3 and DuckDB return the same results"""
        print('SQL input:', input)
        result_sqlite3 = execute_query_sqlite3(input)
        result_duckdb = execute_query_duckdb(input)
        print("SQLite3 output:", result_sqlite3)
        print("DuckDB output:", result_duckdb)
        assert sorted(result_sqlite3) == sorted(result_duckdb)


    @given(cfg("tests/sql/cfgs/sql3.cfg", max_depth=20))
    def test_sql_query_group_by_clause(self, input: str):
        """Property 3: test GROUP BY clause and verify SQLite3 and DuckDB return the same results"""
        print('SQL input:', input)
        result_sqlite3 = execute_query_sqlite3(input)
        result_duckdb = execute_query_duckdb(input)
        print("SQLite3 output:", result_sqlite3)
        print("DuckDB output:", result_duckdb)
        assert sorted(result_sqlite3) == sorted(result_duckdb)

    def tearDown(self) -> None:
        global num_valid_queries
        global num_total_queries
        if num_total_queries == 0:
            num_valid_queries = 1
            num_total_queries = 1
        print('Query validity rate for Hypothesis CFG extension =', num_valid_queries / num_total_queries)
        del_dbs()
        return super().tearDown()

ipytest.run("-s")
