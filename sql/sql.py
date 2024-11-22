import sqlite3

def setup_db():
    """Sets up a SQL DB with tables and data."""
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS table1 (column1 INTEGER, column2 INTEGER, column3 INTEGER, column4 INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS table2 (column1 INTEGER, column2 INTEGER, column3 INTEGER, column4 INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS table3 (column1 INTEGER, column2 INTEGER, column3 INTEGER, column4 INTEGER)")

    for i in range(1, 6):
        cursor.executemany("INSERT INTO table1 VALUES (?, ?, ?, ?)", [(i, i*2, i*3, i*4)])
        cursor.executemany("INSERT INTO table2 VALUES (?, ?, ?, ?)", [(i, i+1, i+2, i+3)])
        cursor.executemany("INSERT INTO table3 VALUES (?, ?, ?, ?)", [(i*2, i*3, i*4, i*5)])

    connection.commit()
    connection.close()

def execute_query(sql_query):
    """Executes a given SQL query"""
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        return f"Error: {e}"
    finally:
        connection.close()

if __name__ == "__main__":
    setup_db()
