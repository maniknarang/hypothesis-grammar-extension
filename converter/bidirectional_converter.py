import argparse
import os
import re


def cfg_to_g4(input):
    '''
        This takes in a cfg file as the input string, parses the string line by
        line to form parser and lexer rules for the corresponding ANTLR g4 file
    '''
    lines = list()
    parser_rules = list()
    lexer_rules = set()
    terminals_map = dict()
    starting_rule = ''

    # Strip input cfg of whitespaces and split into lines for easier g4 conversion
    for line in input.strip().split('\n'):
        line = line.strip()
        lines.append(line)

    for line in lines:
        if ':=' in line:
            lhs, rhs = line.split(':=')
            lhs = lhs.strip()
            rhs = rhs.strip()
            
            # Convert rhs to g4 format; rhs is written in multi-line format
            antlr_rhs = rhs.replace('<', '').replace('>', '')
            antlr_rhs = antlr_rhs.replace('|', '\n    |')
            
            # Grab the starting rule which will be assigned to 'prog' in the corresponding g4 format 
            if lhs == 'S':
                starting_rule = antlr_rhs
                continue
            
            parser_rules.append(f'{lhs} \n    : {antlr_rhs} \n    ;')
            
            # Capture terminals
            for token in rhs.split():
                token = token.strip('<>')
                if token.startswith("'") and token.endswith("'"):
                    value = token.strip("'")
                    if lhs not in terminals_map:
                        terminals_map[lhs] = set()
                    terminals_map[lhs].add(value)
    
    # Add whitespace lexer rule at the end of the file
    lexer_rules.add('WS : [ \\t\\r\\n]+ -> skip ;')
    parser_rules_str = '\n\n'.join(parser_rules)
    lexer_rules_str = '\n\n'.join(lexer_rules)
    
    # Create header for the g4 file and return the final file as a string
    header = f'grammar ConvertedGrammar;\n\n// Start rule\nprog : {starting_rule} EOF ;'
    output = f'{header}\n\n// Parser rules\n{parser_rules_str}\n\n// Lexer rules\n{lexer_rules_str}'

    return output


def g4_to_cfg(input):
    '''
        This takes in a g4 file as the input string and converts it to its corresponding cfg file
    '''
    output = list()

    # Strip .g4 header
    g4_stripped = re.sub(r'grammar\s+\w+;|// Lexer rules.*', '', input, flags=re.DOTALL)
    g4_stripped = g4_stripped.strip()

    # Find all rules from the grammar
    rules = re.findall(r'(\w+)\s*:\s*(.*?)\s*;', g4_stripped, flags=re.DOTALL)

    for rule in rules:
        lhs, rhs = rule
        # Convert starting rule of g4 to cfg format
        if lhs == 'prog':
            lhs = 'S'

        # 1. If the rule has an EOF, strip it out
        # 2. Wrap nonterminals in arrow brackets
        # 3. Put terminals in between single quotes
        # 4. Put multiline rules into single lines
        rhs = re.sub(r'\s*EOF', '', rhs)
        rhs = re.sub(r'([a-zA-Z_][a-zA-Z0-9_]*)', r'<\1>', rhs)
        rhs = re.sub(r'<([a-zA-Z_])>', r'\1', rhs)
        rhs = re.sub(r"'<([^<>]+)>'", r"'\1'", rhs)
        rhs = re.sub(r'\s+', ' ', rhs)

        output.append(f'{lhs} := {rhs}\n')

    output = '\n'.join(output)
    return output


def main():
    parser = argparse.ArgumentParser(description='bi-directional grammar converter for .g4 and .cfg files')
    parser.add_argument('-i', '--input', required=True, help='input .g4 or .cfg file')
    parser.add_argument('-o', '--output_dir', default='.', help='output directory to store converted grammar; default current directory')
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        file = f.read()

    if file and args.input.endswith('cfg'):
        output = cfg_to_g4(file)
        with open(os.path.join(args.output_dir, 'ConvertedGrammar.g4'), 'w') as f:
            f.write(output)
    elif file and args.input.endswith('g4'):
        output = g4_to_cfg(file)
        with open(os.path.join(args.output_dir, 'ConvertedGrammar.cfg'), 'w') as f:
            f.write(output)
    else:
        print(f'File not found or incorrect extension')


if __name__ == "__main__":
    main()
