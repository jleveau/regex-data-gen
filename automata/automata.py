
class NFA:
    it = 0
    EPSILON = "e"

    def __init__(self):
        start = str(NFA.it)
        NFA.it+=1

        final = str(NFA.it)
        NFA.it+=1

        self.start = [start]
        self.final = [final]
        self.transitions = {start: {NFA.EPSILON: [final]}}
        self.states = [start, final]


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

    def addState(self):
        name = NFA.it
        NFA.it+=1
        self.states.append(name)
        return name


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

