from hypothesis.strategies import composite, builds, randoms

from utils import Nonterminal, Terminal


def get_cfg_string(cfg_file_path: str) -> str:
    try:
        with open(cfg_file_path, "r") as f:
            cfg = f.read()
        return cfg
    except FileNotFoundError:
        print(f"File not found: {cfg_file_path}")
        return ""


# needs to be make more robust and be less restrictive
# maybe check fuzzing book to see if they have a better parser
def parse_cfg(
    cfg_string: str,
) -> tuple[
    dict[str, Nonterminal], dict[Nonterminal, list[list[Terminal | Nonterminal]]]
]:
    """
    Takes in CFG's defined with the following format:
    S is the start symbol
    Nonterminals are enclosed in <> (reserved characters)
    Expansions are defined with :=
    Alternatives are separated by |
    Nonterminals must be defined in a single line
    Terminals are not enclosed
    """

    def parse_character_in_expansion(
        expansion_string: str,
    ) -> list[Terminal | Nonterminal]:
        expansion = []
        current_string = None
        for char in expansion_string:
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
        if current_string is not None:
            expansion.append(Terminal(current_string))
        return expansion

    nonterminals = {}
    expansions = {}

    for line in cfg_string.split("\n"):
        if line == "":
            continue

        line = line.split(":=")
        nonterminal = line[0].strip()
        nonterminals[nonterminal] = Nonterminal(nonterminal)
        nonterminal = nonterminals[nonterminal]

        expansions[nonterminal] = []
        for expansion in line[1].strip().split("|"):
            expansions[nonterminal].append(parse_character_in_expansion(expansion))

    return nonterminals, expansions


def get_min_distances(
    nonterminals: dict[str, Nonterminal],
    expansions: dict[Nonterminal, list[list[Terminal | Nonterminal]]],
) -> bool:

    # pass over every nonterminal and check if it has a terminal, set its min distance to 1 and add it to a frontier with distance 1
    frontier = []
    for nonterminal in nonterminals.values():
        nt_expansions = expansions[nonterminal]
        for expansion in nt_expansions:
            if len(expansion) == 1 and isinstance(expansion[0], Terminal):
                nonterminal.set_min_distance_to_terminal(1)
                frontier.append((nonterminal, 1))
                break

        if nonterminal.get_min_distance_to_terminal() is None:
            nonterminal.set_min_distance_to_terminal(float("inf"))

    # Bellman Ford to get the min distances to terminals for each nonterminal
    for _ in range(len(nonterminals)):
        for nonterminal in nonterminals.values():
            for expansion in expansions[nonterminal]:
                distances_to_terminal = []

                for part in expansion:
                    if isinstance(part, Nonterminal):
                        distances_to_terminal.append(
                            nonterminals[
                                part.get_nonterminal()
                            ].get_min_distance_to_terminal()
                            + 1
                        )
                    else:
                        distances_to_terminal.append(1)

                if (
                    max(distances_to_terminal)
                    < nonterminal.get_min_distance_to_terminal()
                ):
                    nonterminal.set_min_distance_to_terminal(max(distances_to_terminal))

    # if a nonterminal has None as min distance, it is unreachable and set it to infty. If any unreachable are found return False else return True
    for nonterminal in nonterminals.values():
        if nonterminal.get_min_distance_to_terminal() == float("inf"):
            return True
    return False


@composite
def generate_string(
    nonterminals: dict[str, Nonterminal],
    expansions: dict[Nonterminal, list[list[Terminal | Nonterminal]]],
    max_depth: int,
) -> str:

    start_symbol = nonterminals["S"]
    current_depth = 0
    # maybe use a custom parse tree class to make the expansions easier
    current_string = [start_symbol]
    next_nonterminal = start_symbol

    print(f"expansions: {expansions}")
    print(f"expansions: {expansions}")

    while current_depth <= max_depth and next_nonterminal != [None]:
        remaining_depth = max_depth - current_depth

        potential_expansions = expansions[next_nonterminal]
        valid_expansions = []
        for expansion in potential_expansions:
            part_depths = []
            for part in expansion:
                if isinstance(part, Nonterminal):
                    part_depths.append(
                        nonterminals[
                            part.get_nonterminal()
                        ].get_min_distance_to_terminal()
                    )
                else:
                    part_depths.append(1)
            expansion_depth = max(part_depths)

            if expansion_depth <= remaining_depth:
                valid_expansions.append(expansion)

        print(f"valid_expansions: {valid_expansions}")
        expansion = random.choice(valid_expansions)
        print(f"chose: {expansion}")
        for i, part in enumerate(expansion):
            if isinstance(part, Nonterminal):
                expansion[i] = nonterminals[part.get_nonterminal()]
        print(f"current string: {current_string}, expansion: {expansion}")

        current_string = (
            current_string[: current_string.index(next_nonterminal)]
            + expansion
            + current_string[current_string.index(next_nonterminal) + 1 :]
        )
        print(f"current string: {current_string}")

        current_depth += 1
        # use default value of next_nonterminal=[None] to break loop if no nonterminal is found
        next_nonterminal = next(
            (part for part in current_string if isinstance(part, Nonterminal)), [None]
        )
        print(f"next_nonterminal: {next_nonterminal}")

    return "".join([str(part) for part in current_string])


@composite
def cfg(draw, cfg_file_path: str = "", max_depth: int = None):

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
    unreachable_detected = get_min_distances(nonterminals, expansions)
    print(f"unreachable_detected: {unreachable_detected}")
    for nonterminal in nonterminals.values():
        print(
            f"{nonterminal.get_nonterminal()} min_distance_to_terminal: {nonterminal.get_min_distance_to_terminal()}"
        )
    # maybe want to warn if max_depth is too low or if theres any unreachable nonterminals?

    # generate random string from grammar w/ max depths
    max_depth = max_depth if max_depth is not None else 10
    result = generate_string(nonterminals, expansions, max_depth)
    print(f"generated: {result}")

    print(f"returning: {result}")
    return result
