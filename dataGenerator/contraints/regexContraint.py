from dataGenerator.contraints.contraint import Constraint
from regex_parser.regex_parser import Parser
from thompson.thompson import Thompson


class RegexConstraint(Constraint):

    def __init__(self, regex):
        super().__init__()
        self.regex = regex

    def buildAutomata(self):
        parser = Parser()
        NFA = Thompson.toNFA(parser.run(self.regex))
        DFA = NFA.NFAtoDFA()
        return DFA
