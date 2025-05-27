from pathlib import Path
from sympy import simplify, sympify
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
                              '-r', 'expr', '-n', '100', '-d', '20', '--sys-path', str(parent_path), '--stdout'],
                              capture_output=True, text=True, check=True)
    samples = [line.strip() for line in samples.stdout.splitlines() if line.strip()]

    return samples

# Hypothesis strategy to choose inputs from samples
test_samples = setup()
print(test_samples)
sample_strategy = st.sampled_from(test_samples)

def simplify_math_expr(math_expr: str) -> str:
    return str(simplify(sympify(math_expr)))

class TestMathExpr(unittest.TestCase):
    @given(sample_strategy, sample_strategy)
    def test_commutative_property(self, expr1, expr2):
        '''
            x + y == y + x
            x * y == y * x
        '''
        print('Expression 1:', expr1)
        print('Expression 2:', expr2)
        result1 = simplify_math_expr(expr1 + '+' + expr2)
        result2 = simplify_math_expr(expr2 + '+' + expr1)
        assert result1 == result2
        result1 = simplify_math_expr('(' + expr1 + ')' + '*' + '(' + expr2 + ')')
        result2 = simplify_math_expr('(' + expr2 + ')' + '*' + '(' + expr1 + ')')
        assert result1 == result2

    @given(sample_strategy)
    def test_identity_property(self, expr):
        '''
            x + 0 == x
            x * 1 == x
        '''
        print('Expression:', expr)
        result1 = simplify_math_expr(expr + '+ 0')
        result2 = simplify_math_expr(expr)
        assert result1 == result2

    @given(sample_strategy)
    def test_subtraction_property(self, expr):
        '''
            x - x == 0
        '''
        print('Expression:', expr)
        result = simplify_math_expr(expr + '-' + '(' + expr + ')')
        assert result == '0'

if __name__ == "__main__":
    unittest.main()
