from regex_parser.regex_parser import Parser
from thompson.thompson import *

if __name__ == "__main__":
    parser = Parser()

    regex1 = "/(a*a*a*ba*b)*/"
    regex2 = "/ba*b/"

    tree1 = parser.run(regex1)
    tree2 = parser.run(regex2)

    NFA1 = Thompson.toNFA(tree1)
    NFA2 = Thompson.toNFA(tree2)


    DFA1 = NFA1.NFAtoDFA()
    DFA2 = NFA2.NFAtoDFA()

    DFA = DFA1.intersection(DFA2)
    file = open("dfa1.dot", "w")
    file.write(DFA.toDot())
    file.close()

    DFA = DFA.minimize()
    file = open("dfa_min.dot", "w")
    file.write(DFA.toDot())
    file.close()

    # DFA2 = NFA2.NFAtoDFA()
    # file = open("dfa2.dot", "w")
    # file.write(DFA2.toDot())
    # file.close()
    #
    # DFA_inter = DFA1.intersection(DFA2)
    # file = open("dfa_inter.dot", "w")
    # file.write(DFA_inter.toDot())
    # file.close()
