
class Automaton:
    it = 0
    EPSILON = "e"

    def __init__(self):
        start = Automaton.it
        Automaton.it+=1

        final = Automaton.it
        Automaton.it+=1

        self.start = [start]
        self.final = [final]
        self.transitions = {start: {Automaton.EPSILON: [final]}}
        self.states = [start, final]
        self.alphabet = []


    def addTransition(self, start, end, literal):
        if not start in self.states :
            raise Exception("Cannot create transition, state does not exists : " + start)
        if not end in self.states :
            raise Exception("Cannot create transition, state does not exists : " + end)

        if not start in self.transitions:
            self.transitions[start] = {}

        if not literal in self.transitions[start]:
            self.transitions[start][literal] = []
        self.transitions[start][literal].append(end)

        if not literal == Automaton.EPSILON and not literal in self.alphabet:
            self.alphabet.append(literal)

    def addState(self):
        name = Automaton.it
        Automaton.it += 1
        self.states.append(name)
        return name

    def determinize(self):
        dfa = Automaton()

        dfa.start = []
        dfa.final = []
        dfa.transitions = {}
        dfa.states = []
        dfa.alphabet = self.alphabet.copy()

        self.start.sort()
        src = tuple(self.start)
        start = src
        powerset = {src: {}}

        toSee = [src]
        it = 0
        while it < len(toSee):
            src = toSee[it]
            for literal in self.alphabet:
                dest = []
                for state in src:
                    if state in self.transitions and literal in self.transitions[state]:
                        for dest_state in self.transitions[state][literal]:
                            if dest_state not in dest:
                               dest.append(dest_state)

                dest.sort()
                dest = tuple(dest)
                powerset[src][literal] = dest
                if len(dest) > 0:
                    if not dest in powerset:
                        powerset[dest] = {}
                        toSee.append(dest)
            it += 1

        states = powerset.keys()
        state_names = {}
        it = 0
        for state in states:
            if state not in state_names:
                state_names[state] = it
            dfa.states.append(it)
            it += 1

            for label in powerset[state]:
                if not powerset[state][label] in state_names:
                    state_names[powerset[state][label]] = it
                    if state_names[powerset[state][label]] not in state_names:
                        dfa.states.append(it)
                        it+=1

                dfa.addTransition(state_names[state], state_names[powerset[state][label]], label)

        dfa.start = [state_names[start]]

        for state in states:
            for sub_state in state:
                if sub_state in self.final and  not state_names[state] in dfa.final:
                    dfa.final.append(state_names[state])
                    break

        return dfa



    def toDot(self):
        graph = {}
        graph["transitions"] = ""
        graph["states"] = ""
        for state in self.states:
            if state in self.start:
                graph["states"] += "\t" + str(state) + ' [label= "' + str(state) + '", color=blue] ' + ';\n'
            elif state in self.final:
                graph["states"] += "\t" + str(state) + ' [label= "' + str(state) + '", color=red] ' + ';\n'
            else :
                graph["states"] += "\t" + str(state) + ' [label= "' + str(state) + '"] ' + ';\n'


        for start in self.transitions.keys():
            for literal in self.transitions[start].keys():
                for end in self.transitions[start][literal]:
                   graph["transitions"] += "\t" + str(start) + " -> " + str(end) + "[label=\"" + literal + "\"]" ";\n"
        return "digraph G { \n"  + graph["states"] + graph["transitions"] + "\n}"

