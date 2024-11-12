class Nonterminal:
    def __init__(self, nonterminal) -> None:
        self._nonterminal = nonterminal
        self._min_distance_to_terminal = None

    def get_nonterminal(self):
        return self._nonterminal

    def get_min_distance_to_terminal(self):
        return self._min_distance_to_terminal

    def set_min_distance_to_terminal(self, min_distance_to_terminal):
        self._min_distance_to_terminal = min_distance_to_terminal

    def __repr__(self) -> str:
        return f"<{self._nonterminal}>"

    def __hash__(self) -> int:
        return hash(self._nonterminal)


class Terminal:
    def __init__(self, terminal) -> None:
        self._terminal = terminal

    def get_terminal(self):
        return self._terminal

    def __repr__(self) -> str:
        return f"{self._terminal}"
