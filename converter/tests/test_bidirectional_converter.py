from hypothesis import given, settings, strategies
import ipaddress
import ipytest
import json
import os
import re
import sys
import tempfile
from sympy import simplify, sympify
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..',)),
)
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "hypothesis_cfg")),
)

from hypothesis_cfg import cfg  # type: ignore
from bidirectional_converter import cfg_to_g4, g4_to_cfg

def setup():
    '''
        This function converts CFG to G4 and back to CFG.
        Converted paths are used to rerun property-based tests.
    '''
    with open('tests/json/cfgs/json.cfg', 'r') as f:
        original_cfg_file = f.read()
        g4_converted_file = cfg_to_g4(original_cfg_file)
        cfg_converted_file = g4_to_cfg(g4_converted_file)

    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.cfg') as tmp1:
            tmp1.write(cfg_converted_file)

    with open('tests/math/cfgs/math_expr.cfg', 'r') as f:
        original_cfg_file = f.read()
        g4_converted_file = cfg_to_g4(original_cfg_file)
        cfg_converted_file = g4_to_cfg(g4_converted_file)

    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.cfg') as tmp2:
            tmp2.write(cfg_converted_file)

    with open('tests/ip/cfgs/ip.cfg', 'r') as f:
        original_cfg_file = f.read()
        g4_converted_file = cfg_to_g4(original_cfg_file)
        cfg_converted_file = g4_to_cfg(g4_converted_file)
        print(cfg_converted_file)

    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.cfg') as tmp3:
            tmp3.write(cfg_converted_file)

    return tmp1.name, tmp2.name, tmp3.name

json_cfg_path, math_expr_cfg_path, ip_cfg_path = setup()

'''
    Helper code to define Hypothesis strategies for math and json test suites
'''
regex = False
def simplify_math_expr(math_expr: str) -> str:
    return str(simplify(sympify(math_expr)))

math_expr_regex = r'^[1-9]+[+\-*/][1-9]+$'
math_expr_strategy = strategies.from_regex(math_expr_regex, fullmatch=True)

def fix_dup_keys_string(json_str: str):
    key_pattern = r'"([^"]+)"\s*:'
    seen_keys = {}

    def replace_key(match):
        key = match.group(1)
        if key in seen_keys:
            seen_keys[key] += 1
            return f'"{key}_{seen_keys[key]}":'
        else:
            seen_keys[key] = 1
            return f'"{key}":'

    modified_json = re.sub(key_pattern, replace_key, json_str)
    return modified_json


def contains_type(json_obj, search_type):
    if isinstance(json_obj, dict):
        for value in json_obj.values():
            if isinstance(value, search_type):
                return True
            if contains_type(value, search_type):
                return True
    return False

json_regex = r'^\{\"([abc]+)\"\:\"([abc]+)\"\}$'
json_strategy = strategies.from_regex(json_regex, fullmatch=True)

'''
    Bidirectional tests that run on CFG files
'''
@given(
    math_expr_strategy if regex else cfg(math_expr_cfg_path, max_depth=20), 
    math_expr_strategy if regex else cfg(math_expr_cfg_path, max_depth=20)
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

@given(math_expr_strategy if regex else cfg(math_expr_cfg_path, max_depth=20))
@settings(deadline=None)
def test_simplify_identity(math_expr: str):
    simplified = simplify_math_expr(math_expr)
    assert simplify_math_expr(math_expr + "+0") == simplified
    assert simplify_math_expr("(" + math_expr + ")*1") == simplified

@given(math_expr_strategy if regex else cfg(math_expr_cfg_path, max_depth=20))
@settings(deadline=None)
def test_simplify_subtraction(math_expr: str):
    assert simplify_math_expr(math_expr + "-(" + math_expr + ")") == "0"

@given(json_str=json_strategy if regex else cfg(json_cfg_path, max_depth=20))
def test_json_inverse(json_str: str):
    print('GENERATED JSON: ', json_str)
    json_str = fix_dup_keys_string(json_str)
    obj = json.loads(json_str)
    assert json.dumps(obj).replace(" ", "") == json_str

@given(json_str=json_strategy if regex else cfg(json_cfg_path, max_depth=20))
def test_json_keys_exist(json_str: str):
    json_str = fix_dup_keys_string(json_str)
    obj = json.loads(json_str)
    for key in obj.keys():
        assert ('"' + key + '"') in json_str

@given(json_str=json_strategy if regex else cfg(json_cfg_path, max_depth=20))
def test_json_dict_list_consistency(json_str: str):
    json_str = fix_dup_keys_string(json_str)
    assert ("[" in json_str) == contains_type(json.loads(json_str), list)
    assert (json_str.count("{") > 1) == contains_type(json.loads(json_str), dict)

@given(cfg(ip_cfg_path, max_depth=20))
def test_ip_inverse(ip: str):
    print('Generated IP: ', ip)
    if ':' in ip:
        ip_address = ipaddress.IPv6Address(ip)
        assert ipaddress.IPv6Address(ip) == ipaddress.IPv6Address(str(ip_address))
    elif '.' in ip:
        ip_address = ipaddress.IPv4Address(ip)
        assert str(ip_address) == ip

@given(cfg(ip_cfg_path, max_depth=20))
def test_ip_in_range(ip: str):
    print('Generated IP', ip)
    if ':' in ip:
        hextets = str(ip).split(':')
        for hectet in hextets:
            for char in hectet:
                assert char.lower() in '0123456789abcdef'
        assert len(hextets) == 8
    elif '.' in ip:
        octets = str(ip).split('.')
        for octet in octets:
            assert 0 <= int(octet) <= 255
        assert len(octets) == 4

ipytest.run("-s")
