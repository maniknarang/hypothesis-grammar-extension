import ipytest
import re
import json
from hypothesis import given, settings
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hypothesis_cfg")),
)

from hypothesis_cfg import cfg  # type: ignore


def fix_dup_keys_string(json_str: str):
    key_pattern = r'(?<!\\)"(.*?)"(?:\s*:)'
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


@given(cfg("tests/cfgs/json.cfg", max_depth=20))
def test_json_inverse(json_str: str):
    json_str = fix_dup_keys_string(json_str)
    obj = json.loads(json_str)
    assert json.dumps(obj).replace(" ", "") == json_str


@given(cfg("tests/cfgs/json.cfg", max_depth=20))
def test_json_keys_exist(json_str: str):
    json_str = fix_dup_keys_string(json_str)
    obj = json.loads(json_str)
    for key in obj.keys():
        assert ('"' + key + '"') in json_str


@given(cfg("tests/cfgs/json.cfg", max_depth=20))
def test_json_dict_list_consistency(json_str: str):
    json_str = fix_dup_keys_string(json_str)
    assert ("[" in json_str) == contains_type(json.loads(json_str), list)
    assert (json_str.count("{") > 1) == contains_type(json.loads(json_str), dict)


ipytest.run("-s")
