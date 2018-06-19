from automata import DFA
from thompson.thompson import Thompson


class Constraint:

    def buildAutomata(self) -> DFA:
        return Thompson.emptyWord()
