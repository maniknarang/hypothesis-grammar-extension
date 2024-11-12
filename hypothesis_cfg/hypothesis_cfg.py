from hypothesis.strategies import composite, builds

from utils import Nonterminal, Terminal


def get_cfg_string(cfg_file_path: str):
    try:
        with open(cfg_file_path, "r") as f:
            cfg = f.read()
        return cfg
    except FileNotFoundError:
        print(f"File not found: {cfg_file_path}")
        return ""


# needs to be make more robust and be less restrictive
# maybe check fuzzing book to see if they have a better parser
def parse_cfg(cfg_string: str):
    """
    Takes in CFG's defined with the following format:
    S is the start symbol
    Nonterminals are enclosed in <> (reserved characters)
    Expansions are defined with :=
    Alternatives are separated by |
    Nonterminals must be defined in a single line
    Terminals are not enclosed
    """

    def parse_character_in_expansion(char, done=False):
        while True:
            expansion = []
            current_string = None
            while not done:
                if char == "<":
                    if current_string is not None:
                        expansion.append(Terminal(current_string))
                        current_string = None
                elif char == ">":
                    if current_string is not None:
                        expansion.append(Nonterminal(current_string))
                        current_string = None
                else:
                    if current_string is None:
                        current_string = ""
                    current_string += char
                yield None
            yield expansions

    nonterminals = set()
    expansions = {}

    for line in cfg_string.split("\n"):
        if line == "":
            continue

        line = line.split(":=")
        nonterminal = Nonterminal(line[0].strip())
        nonterminals.add(nonterminal)

        expansions[nonterminal] = []
        for expansion in line[1].strip().split("|"):
            for char in expansion:
                parse_character_in_expansion(char)
            expansions[nonterminal].append(
                parse_character_in_expansion(None, done=True)
            )

    return nonterminals, expansions


@composite
def cfg(draw, cfg_file_path: str = ""):

    # open file
    print(f"cfg_file_path: {cfg_file_path}")
    cfg_string = get_cfg_string(cfg_file_path)
    if cfg_string == "":
        return ""

    # parse file and get grammar in python classes
    print(f"cfg_string: {cfg_string}")
    nonterminals, expansions = parse_cfg(cfg_string)
    print(f"nonterminals: {nonterminals}")
    print(f"expansions: {expansions}")

    # graph exploration to label min distances to terminals

    # generate random string from grammar w/ max depths

    result = "1+1"
    print(f"returning: {result}")
    return result
