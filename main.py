import os

from regex_parser.regex_parser import Parser
from thompson.thompson import *
import sys

if __name__ == "__main__":
    parser = Parser()

    regex_list = sys.argv
    regex_list.pop(0)

    dfa_list = []
    i = 0
    for regex in regex_list:
        NFA = Thompson.toNFA(parser.run(regex))
        DFA = NFA.NFAtoDFA()
        dfa_list.append(DFA)

        file = open(os.path.join("output", "dfa" + str(i) + ".dot"), "w")
        file.write(DFA.toDot())
        file.close()
        i += 1

    dfa_inter = dfa_list[0]
    for i in range(0, len(dfa_list)):
        dfa_inter = dfa_inter.intersection(dfa_list[i])
    file = open(os.path.join("output", "dfa_inter.dot"), "w")
    file.write(DFA.toDot())
    file.close()

    from subprocess import call
    i = 0
    for dfa in dfa_list:
        print("i : " + dfa.generateWord())
        call(["dot", "-Tpdf", os.path.join("output", "dfa" + str(i) + ".dot"), '-o' , os.path.join("output", "dfa" + str(i) + ".pdf")])
        os.remove( os.path.join("output", "dfa" + str(i) + ".dot"))
        i += 1

    call(["dot", "-Tpdf", os.path.join("output", "dfa_inter.dot"), '-o' , os.path.join("output", "dfa_inter.pdf")])
    os.remove(os.path.join("output", "dfa_inter.dot"))
    print("inter :" + dfa.generateWord())
