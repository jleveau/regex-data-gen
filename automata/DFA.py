from automata.alphabet_iterator import Alphabet
from automata.automata import Automata

def build_new_classes(dfa, equivClass, class_map):

    new_classes = []

    for state1 in equivClass:
        must_create = True
        for new_class in new_classes:
            state2 = new_class[0]
            if state1 == state2:
                continue
            same_class = True
            for label in dfa.alphabet.letters:
                for dest1 in dfa.transitions[state1][label]:
                    for dest2 in dfa.transitions[state2][label]:
                        if class_map[dest1] != class_map[dest2]:
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
    class_map = {}
    for state in dfa.states:
        for i in range(len(equiv_classes)):
            if state in equiv_classes[i]:
                class_map[state] = i

    for equiv_class in equiv_classes:
        new_equiv_classes += build_new_classes(dfa, equiv_class, class_map)

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
    new_dfa = DFA(Alphabet())
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
            for dest in dfa.transitions[state][label]:
                new_dfa.addTransition(state_dict[state], state_dict[dest], label)

    for final_state in dfa.final:
        new_dfa.final.add(state_dict[final_state])

    new_dfa.start = set()
    for start_state in dfa.start:
        new_dfa.start.add(state_dict[start_state])
    return new_dfa

class DFA(Automata):

    def __init__(self, alphabet):
        super().__init__(alphabet)

    def negation(self) -> 'DFA':
        new_dfa = DFA(Alphabet())
        equiv_states = {}
        for state in self.states:
            equiv_states[state] = new_dfa.addState()

        new_dfa.start = set()
        for start in self.start:
            new_dfa.start.add(equiv_states[start])

        for state in self.states:
            if state not in self.final:
                new_dfa.final.add(equiv_states[state])

        for state in self.states:
            for label in self.transitions[state]:
                for dest in self.transitions[state][label]:
                    new_dfa.addTransition(equiv_states[state], equiv_states[dest], label)
        return new_dfa

    def union(self, dfa) -> 'DFA':
        from automata.NFA import NFA
        union_nfa = NFA(Alphabet({Automata.EPSILON}))

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
        union_nfa.start = {start}

        for start_state in self.start:
            union_nfa.addTransition(start, equiv_states[start_state], Automata.EPSILON)

        for start_state in dfa.start:
            union_nfa.addTransition(start, equiv_states[start_state], Automata.EPSILON)

        for final_state in dfa.final.union(self.final):
            union_nfa.final.add(equiv_states[final_state])
        union_nfa.final = union_nfa.final.union(dfa.final)

        union_nfa = union_nfa.removeEpsilon()
        return union_nfa.NFAtoDFA()

    def intersection(self, dfa):
        neg_dfa1 = self.negation()
        neg_dfa2 = dfa.negation()
        union = neg_dfa1.union(neg_dfa2)
        inter = union.negation()

        return inter

    def minimize(self):
        if self.final == self.states:
            equiv_classes = [self.final]
        else:
            equiv_classes = [
                self.states - self.final,
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














