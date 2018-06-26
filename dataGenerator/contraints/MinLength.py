from automata.DFA import DFA
from automata.alphabet_iterator import Alphabet
from dataGenerator.contraints.contraint import Constraint
from regex_parser.regex_parser import Parser
from thompson.automatonbuilder import AutomatonBuilder


class MinLength(Constraint):

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
            for i in range(self.length-1):
                state = dfa.addState()
                for label in dfa.alphabet:
                    dfa.addTransition(previous, state, label)
                previous = state

            end = dfa.addState()
            for label in dfa.alphabet:
                dfa.addTransition(previous, end, label)
            for label in dfa.alphabet:
                dfa.addTransition(end, end, label)
            dfa.final.add(end)
            return dfa

    def getTitle(self):
        return "must have length superior to : " + str(self.length)