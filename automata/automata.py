def hasPathFromStartRec(nfa, target, current, visited):

    visited.append(current)
    if current == target:
        return True

    if current not in nfa.transitions:
        return

    for label in nfa.transitions[current]:
        for dest in nfa.transitions[current][label]:
            if dest not in visited:
                if hasPathFromStartRec(nfa, target, dest, visited):
                    return True
    return False


def findPathFromStart(nfa, state):
    if state in nfa.start:
        return True
    for start in nfa.start:
        word = []
        if hasPathFromStartRec(nfa, state, start, []):
            return str(word.reverse())
    return False

def generateWordRec(nfa, current, target, visited, word):
    if current == target:
        return True
    visited.append(current)
    for state in nfa.transitions:
        for label in nfa.transitions[current]:
            for dest in nfa.transitions[current][label]:
                if dest not in visited:
                    if generateWordRec(nfa, dest, target, visited, word):
                        word += [label]
                        return True
    return False

class Automata:

    def __init__(self, alphabet):
        self.start = set()
        self.final = set()
        self.transitions = {}
        self.states = set()
        self.alphabet = alphabet
        self.empty_transition = {}

    it = 0
    EPSILON = "epsilon"


    def addTransition(self, start, end, literal):
        self.transitions[start][literal].add(end)

    def addState(self):
        Automata.it += 1
        name = str(Automata.it)
        self.states.add(name)
        self.transitions[name] = {}
        for literal in self.alphabet:
            self.transitions[name][literal] = set()
        return name


    def hasFinalState(self) -> bool:
        return len(self.final) > 0

    def toDot(self):
        graph = {"transitions": "",
                 "states": ""}
        for state in self.states:
            if state in self.start and state in self.final:
                graph["states"] += "\t" + str(state) + ' [label= "' + str(state) + '", color=purple] ' + ';\n'
            elif state in self.start:
                graph["states"] += "\t" + str(state) + ' [label= "' + str(state) + '", color=blue] ' + ';\n'
            elif state in self.final:
                graph["states"] += "\t" + str(state) + ' [label= "' + str(state) + '", color=red] ' + ';\n'
            else :
                graph["states"] += "\t" + str(state) + ' [label= "' + str(state) + '"] ' + ';\n'

        transitions = {}

        for state in self.transitions.keys():
            transitions[state] = {}
            for literal in self.transitions[state].keys():
                for dest in self.transitions[state][literal]:
                    if dest not in transitions[state]:
                        transitions[state][dest] = []
                    transitions[state][dest].append(literal)

        for state in transitions:
            for dest in transitions[state]:
                s = ""
                i = 0

                for label in transitions[state][dest]:
                    s += str(label) + " "
                    i+=1
                    if i >= 5:
                        s += "... [" + str(len(transitions[state][dest])) + ']'
                        break

                graph["transitions"] += "\t" + str(state) + " -> " + str(dest) + "[label=\"" + ascii(s) + "\"]" ";\n"

        return "digraph G { \n"  + graph["states"] + graph["transitions"] + "\n}"

    def printPDF(self, name, dir):
        import os
        file = open(os.path.join(dir, name + ".dot"), "w")
        file.write(self.toDot())
        file.close()
        from subprocess import call
        call(["dot", "-Tpdf", os.path.join(dir, name +".dot"), '-o', os.path.join(dir, name + ".pdf")])
        os.remove(os.path.join(dir, name + ".dot"))


    def generateWord(self):
        word = []
        if len(self.final) == 0:
            return "cannot create word"
        generateWordRec(self, list(self.start)[0], list(self.final)[0], [], word)
        word.reverse()
        return ''.join(word)
