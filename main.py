from regex_parser.regex_parser import Parser
from thompson.thompson import *

if __name__ == "__main__":
    parser = Parser()
    regex = "/aa/"
    NFA = None
    if not regex or regex == "//":
        NFA = Thompson.emptyWord()
    else :
        tree = parser.run(regex)
        file = open("regex.dot", "w")
        file.write(tree.toDot())
        file.close()
        NFA = Thompson.toNFA(tree)

    file = open("nfa.dot", "w")
    file.write(NFA.toDot())
    file.close()
