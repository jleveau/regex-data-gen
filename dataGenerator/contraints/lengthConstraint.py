from dataGenerator.contraints.contraint import Constraint
from regex_parser.regex_parser import Parser
from thompson.thompson import Thompson


class LengthConstraint(Constraint):

    def __init__(self, length: int):
        super().__init__()
        self.length = length

    def buildAutomata(self):
        regex = ""
        for i in range(self.length):
            regex += "[a-d]"

        parser = Parser()
        NFA = Thompson.toNFA(parser.run('/' + regex + '/'))
        DFA = NFA.NFAtoDFA()
        return DFA
