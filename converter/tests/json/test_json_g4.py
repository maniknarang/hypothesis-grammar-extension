import json
from pathlib import Path
import re
import subprocess
import unittest

from hypothesis import given, strategies as st

def setup():
    '''
        Run grammarinator to create for the g4 file and generate samples for testing
    '''
    parent_path = Path(__file__).parent

    subprocess.run(['grammarinator-process', str(parent_path) + '/ConvertedGrammar.g4',
                    '-o', str(parent_path), '--no-actions'],
                    check=True)

    samples = subprocess.run(['grammarinator-generate',
                              'ConvertedGrammarGenerator.ConvertedGrammarGenerator',
                              '-r', 'json', '-n', '100', '-d', '20', '--sys-path', str(parent_path), '--stdout'],
                              capture_output=True, text=True, check=True)
    samples = [line.strip() for line in samples.stdout.splitlines() if line.strip()]

    return samples

# Hypothesis strategy to choose inputs from samples
test_samples = setup()
print(test_samples)
sample_strategy = st.sampled_from(test_samples)

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

class TestJson(unittest.TestCase):
    @given(sample_strategy)
    def test_json_inverse(self, json_str):
        print('Generated JSON: ', json_str)
        json_str = fix_dup_keys_string(json_str)
        obj = json.loads(json_str)
        assert json.dumps(obj).replace(" ", "") == json_str

    @given(sample_strategy)
    def test_json_keys_exist(self, json_str):
        print('Generated JSON: ', json_str)
        json_str = fix_dup_keys_string(json_str)
        obj = json.loads(json_str)
        for key in obj.keys():
            assert ('"' + key + '"') in json_str

    @given(sample_strategy)
    def test_json_dict_list_consistency(self, json_str):
        print('Generated JSON: ', json_str)
        json_str = fix_dup_keys_string(json_str)
        assert ("[" in json_str) == contains_type(json.loads(json_str), list)
        assert (json_str.count("{") > 1) == contains_type(json.loads(json_str), dict)
