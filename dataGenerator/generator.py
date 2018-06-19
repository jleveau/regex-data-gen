from automata import DFA
from dataGenerator.contraints.contraint import Constraint


def buildAutomata(constraints) -> DFA:
    if len(constraints) == 0:
        return None
    automata = constraints[0].buildAutomata()
    automata.printPDF("0")

    if len(constraints) == 1:
        return automata
    for i in range(1, len(constraints)):
        automata2 = constraints[i].buildAutomata()
        automata2.printPDF(str(i))

        automata = automata.intersection(automata2)
    return automata


class DataGenerator:

    def __init__(self):
        self.constraints = []

    def addConstraint(self, constraint: Constraint):
        self.constraints.append(constraint)

    def generate(self) -> str:
        automata = buildAutomata(self.constraints)
        automata.printPDF("reg")
        if not automata.hasFinalState():
            print("cannot match all constraints")
            return ""
        return automata.generateWord()
