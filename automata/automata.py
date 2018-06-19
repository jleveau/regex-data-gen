from automata.alphabet_iterator import Alphabet


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

    def __init__(self):
        self.start = []
        self.final = []
        self.transitions = {}
        self.states = []
        self.alphabet = Alphabet()

    it = 0
    EPSILON = "epsilon"

    def addTransition(self, start, end, literal):
        if start not in self.states :
            raise Exception("Cannot create transition, state does not exists : " + str(start))
        if end not in self.states :
            raise Exception("Cannot create transition, state does not exists : " + str(end))
        self.alphabet.addToAlphabet(literal)
        if start not in self.transitions:
            self.transitions[start] = {}
        if literal not in self.transitions[start]:
            self.transitions[start][literal] = []
        if end not in self.transitions[start][literal]:
            self.transitions[start][literal].append(end)
        return


    def addState(self):
        Automata.it += 1
        name = str(Automata.it)
        self.states.append(name)
        return name

    def removeState(self, state):
        if not state in self.states:
            raise Exception("State not in states list")
        self.states.remove(state)
        if state in self.transitions:
            self.transitions.pop(state)
        for state_src in self.states:
            if state_src  in self.transitions:
                for literal in self.transitions[state_src]:
                    if state in self.transitions[state_src][literal]:
                        self.transitions[state_src][literal].remove(state)

    def removeUnReachableState(self):
        to_remove = set()

        # Remove unreachable states
        for state in self.states:
            if not findPathFromStart(self, state):
                to_remove.add(state)

        for state in to_remove:
            if state in self.start:
                self.start.remove(state)
            if state in self.final:
                self.final.remove(state)
            self.removeState(state)

    def copyState(self, src: 'Automata'):
        for state in src.states:
            if not state in self.states:
                self.states.append(state)

    def copyTransition(self, src: 'Automata'):
        for start in src.transitions.keys():
            for literal in src.transitions[start].keys():
                for final in src.transitions[start][literal]:
                    self.addTransition(start, final, literal)

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

    def printPDF(self, name):
        import os
        file = open(os.path.join("output", name + ".dot"), "w")
        file.write(self.toDot())
        file.close()
        from subprocess import call
        call(["dot", "-Tpdf", os.path.join("output", name +".dot"), '-o', os.path.join("output", name + ".pdf")])
        os.remove(os.path.join("output", name + ".dot"))


    def generateWord(self):
        if len(self.start) == 0:
            raise Exception("no start state")
        if len(self.final) == 0:
            raise Exception("no start state")
        word = []
        generateWordRec(self, self.start[0], self.final[0], [], word)
        word.reverse()
        return ''.join(word)
