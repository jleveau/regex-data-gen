from automata import DFA
from dataGenerator.contraints.contraint import Constraint


def createDataFromConstraints(constraints, invert_it):
    if invert_it == 0:
        automata = constraints[0].buildInvertAutomata()
    else:
        automata = constraints[0].buildAutomata()

    if len(constraints) == 1:
        return automata.generateWord()

    for i in range(1, len(constraints)):
        if i != invert_it:
            automata2 = constraints[i].buildAutomata()
        else:
            automata2 = constraints[i].buildInvertAutomata()
        inter = automata.intersection(automata2)
        automata = inter.minimize()

    return automata.generateWord()


def createTitleFromConstraint(constraints, invert_it):
    title = ""
    for i in range(len(constraints)):
        constraint_title = constraints[i].getTitle()
        if invert_it == i:
            constraint_title = "NOT " + constraint_title
        title += constraint_title + "\n"
    return title


class DataGenerator:

    def __init__(self):
        self.constraints = []

    def addConstraint(self, constraint: Constraint):
        self.constraints.append(constraint)

    def generate(self):
        result = [tuple([createTitleFromConstraint(self.constraints, -1),
                         createDataFromConstraints(self.constraints, -1)])]

        for i in range(len(self.constraints)):
            result.append([createTitleFromConstraint(self.constraints, i),
                           createDataFromConstraints(self.constraints, i)])

        return result
