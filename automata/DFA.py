from automata.automata import Automata

def build_new_classes(dfa, equivClass):

    new_classes = [[equivClass[0]]]
    for state1 in equivClass:
        if state1 == equivClass[0]:
            continue

        must_create = True
        for new_class in new_classes:
            state2 = new_class[0]
            if state1 == state2:
                continue
            same_class = True
            for label in dfa.alphabet.letters:
                if dfa.transitions[state1][label][0] != dfa.transitions[state2][label][0]:
                    same_class = False
                    break
            if same_class:
                new_class.append(state1)
                must_create = False
                break

        if must_create:
            new_classes.append([state1])
    return new_classes


def updateEquivalenceClasses(dfa: 'DFA', equiv_classes):
    new_equiv_classes = []
    for equiv_class in equiv_classes:
        new_equiv_classes += build_new_classes(dfa, equiv_class)

    return new_equiv_classes

def getEquivClassForState(state, classes):
    for equiv_class in classes:
        if state in equiv_class:
            return equiv_class

def classChanged(dfa: 'DFA', classes1, classes2):
    for state in dfa.states:
        equiv_class1 = getEquivClassForState(state, classes1)
        equiv_class2 = getEquivClassForState(state, classes2)
        classes1_set = set(equiv_class1)
        classes2_set = set(equiv_class2)
        if classes1_set != classes2_set:
            return True
    return False




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


        union = neg_dfa1.union(neg_dfa2)

        inter = union.negation()

        min = inter.minimize()
        return min

    def minimize(self):
        equiv_classes = [
            list(set(self.states) - set(self.final)),
            self.final.copy()]
        has_change = True
        while has_change:
            has_change = False
            classes = equiv_classes.copy()
            new_equiv_classes = updateEquivalenceClasses(self, equiv_classes)

            if classChanged(self, classes, new_equiv_classes):
                has_change = True
            equiv_classes = new_equiv_classes

        return createFromEquivClasses(self, equiv_classes)














