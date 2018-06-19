from automata.automata import Automata

def updateEquivalenceClasses(dfa: 'DFA', state, new_equiv_classes, equiv_classes):
    class_found = False
    old_class = None
    for i in range(len(equiv_classes)):
        if state in equiv_classes[i]:
            old_class = i
    for i in range(len(equiv_classes)):
        if len(equiv_classes[i]) == 1 and equiv_classes[i][0] == state:
            new_equiv_classes.append([state])
            class_found = True
            break
        isInClass = True

        state2 = equiv_classes[i][0]
        if state == state2:
            continue

        for label in dfa.transitions[state]:
            for dest in dfa.transitions[state][label]:
                dest_class = None
                for i in range(len(equiv_classes)):
                    if dest in equiv_classes[i]:
                        dest_class = i
                if dest_class == old_class:
                    isInClass = False
                    break

            if not isInClass:
                break
        if isInClass:
            if i >= len(new_equiv_classes):
                new_equiv_classes.append([state])
            else :
                new_equiv_classes[i].append(state)
            class_found = True
            break

    if not class_found:
        new_equiv_classes.append([state])

    return new_equiv_classes



def createFromEquivClasses(dfa: 'DFA', equiv_classes) -> 'DFA':
    new_dfa = DFA()
    names = []
    state_dict = {}
    for i in range(len(equiv_classes)):
        names.append(new_dfa.addState())

    for state in dfa.states:
        for i in range(len(equiv_classes)):
            if state in equiv_classes[i]:
                state_dict[state] = names[i]

    for state in dfa.states:
        for label in dfa.alphabet:
            new_dfa.addTransition(state_dict[state], state_dict[dfa.transitions[state][label][0]], label)

    for final_state in dfa.final:
        new_dfa.final.append(state_dict[final_state])
    new_dfa.start = [state_dict[dfa.start[0]]]
    return new_dfa

class DFA(Automata):

    def __init__(self):
        super().__init__()

    def negation(self) -> 'DFA':
        new_dfa = DFA()
        equiv_states = {}
        for state in self.states:
            equiv_states[state] = new_dfa.addState()

        new_dfa.start = []
        for start in self.start:
            new_dfa.start.append(equiv_states[start])

        for state in self.states:
            if state not in self.final:
                new_dfa.final.append(equiv_states[state])

        for state in self.states:
            for label in self.transitions[state]:
                for dest in self.transitions[state][label]:
                    new_dfa.addTransition(equiv_states[state], equiv_states[dest], label)
        return new_dfa

    def union(self, dfa) -> 'DFA':
        from automata.NFA import NFA
        union_nfa = NFA()

        equiv_states = {}

        for state in self.states:
            equiv_states[state] = union_nfa.addState()

        for state in self.transitions:
            for literal in self.transitions[state]:
                for dest in self.transitions[state][literal]:
                    union_nfa.addTransition(equiv_states[state], equiv_states[dest], literal)

        for state in dfa.states:
            equiv_states[state] = union_nfa.addState()

        for state in dfa.transitions:
            for literal in dfa.transitions[state]:
                for dest in dfa.transitions[state][literal]:
                    union_nfa.addTransition(equiv_states[state], equiv_states[dest], literal)

        start = union_nfa.addState()
        union_nfa.start = [start]
        union_nfa.addTransition(start, equiv_states[self.start[0]], Automata.EPSILON)
        union_nfa.addTransition(start, equiv_states[dfa.start[0]], Automata.EPSILON)

        for final_state in dfa.final + self.final:
            union_nfa.final.append(equiv_states[final_state])
        union_nfa.final += dfa.final

        union_nfa = union_nfa.removeEpsilon()
        return union_nfa.NFAtoDFA()

    def intersection(self, dfa):
        neg_dfa1 = self.negation()
        neg_dfa2 = dfa.negation()
        print(neg_dfa1.alphabet.letters.difference(neg_dfa2.alphabet.letters))
        union = neg_dfa1.union(neg_dfa2)
        inter = union.negation()
        return inter.minimize()


    def minimize(self):
        equiv_classes = [[], []]
        equiv_classes[0] = list(set(self.states) - set(self.final))
        equiv_classes[1] = self.final.copy()

        while True:
            new_equiv_classes = []
            for state in self.states:
                new_equiv_classes = updateEquivalenceClasses(self, state, new_equiv_classes, equiv_classes)
            if len(equiv_classes) == len(new_equiv_classes):
                break
            equiv_classes = new_equiv_classes
        return createFromEquivClasses(self, equiv_classes)














