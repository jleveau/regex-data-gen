def hasPathFromStartRec(nfa, target, current, visited):

    visited.append(current)
    if current == target:
        return True

    if not current in nfa.transitions:
        return

    for label in nfa.transitions[current]:
        for dest in nfa.transitions[current][label]:
            if not dest in visited:
                if hasPathFromStartRec(nfa, target, dest, visited):
                    return True
    return False


def hasPathFromStart(nfa, state):
    if state in nfa.start:
        return True
    for start in nfa.start:
        if hasPathFromStartRec(nfa, state, start, []):
            return True
    return False

class Automata:

    def __init__(self):
        self.start = []
        self.final = []
        self.transitions = {}
        self.states = []

    it = 0
    EPSILON = "e"

    def addTransition(self, start, end, literal):
        if not start in self.states :
            raise Exception("Cannot create transition, state does not exists : " + str(start))
        if not end in self.states :
            raise Exception("Cannot create transition, state does not exists : " + str(end))

        if not start in self.transitions:
            self.transitions[start] = {}
        if not literal in self.transitions[start]:
            self.transitions[start][literal] = []
        if not end in  self.transitions[start][literal]:
            self.transitions[start][literal].append(end)
        return


    def addState(self):
        Automata.it += 1
        name = Automata.it
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
            if not hasPathFromStart(self, state):
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

    def toDot(self):
        graph = {}
        graph["transitions"] = ""
        graph["states"] = ""
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
                if len(transitions[state][dest]) > 4:
                    s = "..."
                else:
                    for label in transitions[state][dest]:
                        if isinstance(label, str):
                            s += label
                        else:
                          s += chr(label) + " "
                        i+=1
                        if i > 5:
                            s += "..."
                            break

                graph["transitions"] += "\t" + str(state) + " -> " + str(dest) + "[label=\"" + ascii(s) + "\"]" ";\n"

        return "digraph G { \n"  + graph["states"] + graph["transitions"] + "\n}"

