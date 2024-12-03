# Regular Hypothesis
```
pytest just_hypothesis.py -s
```

# Extension Usage
```
pytest tests/parser/test_simple.py -s
```
```
pytest tests/parser/test_recursive.py -s
```

# Parser Internals
***Set DEBUG=True***
```
pytest tests/parser/test_simple.py -s
```
***Set DEBUG=False***

# SQL
...
```
pytest -sk test_sql_query_syntax
```

```
pytest -sk test_sql_query_where_clause
```

```
pytest -sk test_sql_query_group_by_clause
```

***Negative GROUP BY test:***
```
input = "SELECT * from table1 GROUP BY column1;"
```


# JSON
...


# Math Expressions
...


# HTTP
...


# Binary Trees
```
pytest tests/binary_tree/test_BT.py -s
pytest tests/binary_tree/test_BST.py -s
```

