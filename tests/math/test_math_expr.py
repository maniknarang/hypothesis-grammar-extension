from sympy import simplify, sympify
import ipytest
from hypothesis import given, settings
from hypothesis import strategies as st
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "hypothesis_cfg")),
)

from hypothesis_cfg import cfg  # type: ignore

regex = False

def simplify_math_expr(math_expr: str) -> str:
    return str(simplify(sympify(math_expr)))

math_expr_regex = r'^[1-9]+[+\-*/][1-9]+$'
math_expr_strategy = st.from_regex(math_expr_regex, fullmatch=True)

@given(
    math_expr_strategy if regex else cfg("tests/math/cfgs/math_expr.cfg", max_depth=20), 
    math_expr_strategy if regex else cfg("tests/math/cfgs/math_expr.cfg", max_depth=20)
)
@settings(deadline=None)
def test_simplify_communative(math_expr: str, math_expr2: str):
    print("GENERATED MATH EXPR 1: ", math_expr)
    print("GENERATED MATH EXPR 2: ", math_expr2)
    assert simplify_math_expr(math_expr + "+" + math_expr2) == simplify_math_expr(
        math_expr2 + "+" + math_expr
    )
    assert simplify_math_expr(
        "(" + math_expr + ")*(" + math_expr2 + ")"
    ) == simplify_math_expr("(" + math_expr2 + ")*(" + math_expr + ")")

@given(math_expr_strategy if regex else cfg("tests/math/cfgs/math_expr.cfg", max_depth=20))
@settings(deadline=None)
def test_simplify_identity(math_expr: str):
    simplified = simplify_math_expr(math_expr)
    assert simplify_math_expr(math_expr + "+0") == simplified
    assert simplify_math_expr("(" + math_expr + ")*1") == simplified

@given(math_expr_strategy if regex else cfg("tests/math/cfgs/math_expr.cfg", max_depth=20))
@settings(deadline=None)
def test_simplify_subtraction(math_expr: str):
    assert simplify_math_expr(math_expr + "-(" + math_expr + ")") == "0"


ipytest.run("-s")
