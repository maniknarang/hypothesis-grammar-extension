import os
import sqlite3
import duckdb
from hypothesis import given, strategies as st

DB_DIR = 'sql'
SQLITE3_DB_PATH = os.path.join(DB_DIR, 'test.db')
DUCKDB_PATH = os.path.join(DB_DIR, 'test.duckdb')
num_valid_queries = 0
num_total_queries = 0

def setup_dbs():
    """Sets up SQL DBs with tables and data."""
    os.makedirs(DB_DIR, exist_ok=True)
    connection_sqlite3 = sqlite3.connect(SQLITE3_DB_PATH)
    connection_duckdb = duckdb.connect(DUCKDB_PATH)
    cursor_sqlite3 = connection_sqlite3.cursor()
    cursor_duckdb = connection_duckdb.cursor()

    cursor_sqlite3.execute('CREATE TABLE IF NOT EXISTS table1 (column1 INTEGER, column2 INTEGER, column3 INTEGER, column4 INTEGER)')
    cursor_sqlite3.execute('CREATE TABLE IF NOT EXISTS table2 (column1 INTEGER, column2 INTEGER, column3 INTEGER, column4 INTEGER)')
    cursor_sqlite3.execute('CREATE TABLE IF NOT EXISTS table3 (column1 INTEGER, column2 INTEGER, column3 INTEGER, column4 INTEGER)')
    cursor_duckdb.execute('CREATE TABLE IF NOT EXISTS table1 (column1 INTEGER, column2 INTEGER, column3 INTEGER, column4 INTEGER)')
    cursor_duckdb.execute('CREATE TABLE IF NOT EXISTS table2 (column1 INTEGER, column2 INTEGER, column3 INTEGER, column4 INTEGER)')
    cursor_duckdb.execute('CREATE TABLE IF NOT EXISTS table3 (column1 INTEGER, column2 INTEGER, column3 INTEGER, column4 INTEGER)')

    for i in range(10):
        cursor_sqlite3.executemany('INSERT INTO table1 VALUES (?, ?, ?, ?)', [(i, i * 2, i * 3, i * 4)])
        cursor_sqlite3.executemany('INSERT INTO table2 VALUES (?, ?, ?, ?)', [(i ** 2, (i + 1) ** 2, (i + 2) ** 2, (i + 3) ** 2)])
        cursor_sqlite3.executemany('INSERT INTO table3 VALUES (?, ?, ?, ?)', [(i * i, i * (i + 1), i * (i + 2), i * (i + 3))])
        cursor_duckdb.executemany('INSERT INTO table1 VALUES (?, ?, ?, ?)', [(i, i * 2, i * 3, i * 4)])
        cursor_duckdb.executemany('INSERT INTO table2 VALUES (?, ?, ?, ?)', [(i ** 2, (i + 1) ** 2, (i + 2) ** 2, (i + 3) ** 2)])
        cursor_duckdb.executemany('INSERT INTO table3 VALUES (?, ?, ?, ?)', [(i * i, i * (i + 1), i * (i + 2), i * (i + 3))])

    connection_sqlite3.commit()
    connection_sqlite3.close()
    connection_duckdb.commit()
    connection_duckdb.close()

def sql_strategy():
    """Define SQL strategy for Hypothesis baseline. This same grammar is emulated in tests/sql/cfgs/sql1.cfg"""
    column = st.sampled_from(['column1', 'column2', 'column3', 'column4'])
    table = st.sampled_from(['table1', 'table2', 'table3'])
    operator = st.sampled_from(['=', '>', '<', '>=', '<='])
    value = st.sampled_from(['1', '2', '3'])
    order_direction = st.sampled_from(['ASC', 'DESC'])

    condition = st.recursive(
        base=st.tuples(column, operator, value).map(lambda t: f"{t[0]} {t[1]} {t[2]}"),
        extend=lambda inner: st.one_of(
            inner.map(lambda c: f'({c})'),
            st.tuples(inner, st.just('AND'), inner).map(lambda t: f'{t[0]} AND {t[2]}'),
            st.tuples(inner, st.just('OR'), inner).map(lambda t: f'{t[0]} OR {t[2]}'),
        ),
        max_leaves=5,
    )

    items = st.one_of(
        st.just('*'),
        st.lists(column, min_size=1, max_size=4).map(lambda cols: ", ".join(cols))
    )
    from_clause = table.map(lambda t: f'FROM {t}')
    where_clause = st.one_of(condition.map(lambda c: f'WHERE {c}'), st.just(''))
    group_by_clause = st.one_of(column.map(lambda c: f'GROUP BY {c}'), st.just(''))
    order_by_clause = st.one_of(
        st.tuples(column, order_direction).map(lambda t: f'ORDER BY {t[0]} {t[1]}'),
        st.just('')
    )

    select_statement = st.tuples(
        items, from_clause, where_clause, group_by_clause, order_by_clause
    ).map(lambda parts: f'SELECT {parts[0]} {parts[1]} {parts[2]} {parts[3]} {parts[4]};')

    return select_statement

def execute_query(query):
    """Executes a given SQL query on SQLite3 and DuckDB"""
    try:
        connection_sqlite3 = sqlite3.connect(SQLITE3_DB_PATH)
        connection_duckdb = duckdb.connect(DUCKDB_PATH)
        sqlite_result = connection_sqlite3.execute(query).fetchall()
        duckdb_result = connection_duckdb.execute(query).fetchall()
        connection_sqlite3.close()
        connection_duckdb.close()
        return sqlite_result, duckdb_result
    except Exception:
        return None, None

@given(sql_query=sql_strategy())
def test_sql_baseline(sql_query):
    global num_valid_queries
    global num_total_queries
    num_total_queries += 1
    print('SQL_QUERY', sql_query)

    sqlite_result, duckdb_result = execute_query(sql_query)
    if sqlite_result is not None and duckdb_result is not None:
        num_valid_queries += 1

def del_dbs():
    os.remove(SQLITE3_DB_PATH)
    os.remove(DUCKDB_PATH)

if __name__ == "__main__":
    setup_dbs()

    test_sql_baseline()

    print('Query validity rate for Hypothesis baseline =', num_valid_queries / num_total_queries)

    del_dbs()
