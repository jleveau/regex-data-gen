from automata import DFA
from thompson.automatonbuilder import AutomatonBuilder


class Constraint:

    def buildAutomata(self) -> DFA:
        return AutomatonBuilder.emptyWord()

    def getTitle(self) -> str:
        return "empty constraint"

    def buildInvertAutomata(self) -> DFA:
        return self.buildAutomata().negation()