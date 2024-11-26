from sympy import simplify, sympify
import ipytest
from hypothesis import given, settings
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hypothesis_cfg")),
)

from hypothesis_cfg import cfg  # type: ignore


def simplify_math_expr(math_expr: str) -> str:
    try:
        return str(simplify(sympify(math_expr)))
    except Exception as e:
        return f"Error:{e}"


@given(
    cfg("tests/cfgs/math_expr.cfg", max_depth=20),
    cfg("tests/cfgs/math_expr.cfg", max_depth=20),
)
@settings(deadline=None)
def test_simplify_communative(math_expr: str, math_expr2: str):
    assert simplify_math_expr(math_expr + "+" + math_expr2) == simplify_math_expr(
        math_expr2 + "+" + math_expr
    )
    assert simplify_math_expr(
        "(" + math_expr + ")*(" + math_expr2 + ")"
    ) == simplify_math_expr("(" + math_expr2 + ")*(" + math_expr + ")")


@given(cfg("tests/cfgs/math_expr.cfg", max_depth=20))
@settings(deadline=None)
def test_simplify_identity(math_expr: str):
    simplified = simplify_math_expr(math_expr)
    assert simplify_math_expr(math_expr + "+0") == simplified
    assert simplify_math_expr("(" + math_expr + ")*1") == simplified


@given(cfg("tests/cfgs/math_expr.cfg", max_depth=20))
@settings(deadline=None)
def test_simplify_subtraction(math_expr: str):
    assert simplify_math_expr(math_expr + "-(" + math_expr + ")") == "0"


ipytest.run("-s")
