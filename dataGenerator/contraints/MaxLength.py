from automata.alphabet_iterator import Alphabet
from dataGenerator.contraints.contraint import Constraint
from regex_parser.regex_parser import Parser
from thompson.automatonbuilder import AutomatonBuilder
from automata.DFA import DFA

class MaxLength(Constraint):

    def __init__(self, length: int):
        super().__init__()
        self.length = length

    def buildAutomata(self):
        if self.length == 0:
            return AutomatonBuilder.emptyWord()
        else :
            dfa = DFA(Alphabet())
            start = dfa.addState()
            previous = start
            dfa.start.add(start)
            dfa.final.add(start)
            for i in range(self.length):
                state = dfa.addState()
                for label in dfa.alphabet:
                    dfa.addTransition(previous, state, label)
                dfa.final.add(state)
                previous = state

            end = dfa.addState()
            for label in dfa.alphabet:
                dfa.addTransition(previous, end, label)
            for label in dfa.alphabet:
                dfa.addTransition(end, end, label)
            return dfa

    def getTitle(self):
        return "must have length inferior to : " + str(self.length)