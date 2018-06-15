from automata.automata import Automata



class DFA(Automata):

    def __init__(self):
        super().__init__()

    def negation(self) -> 'DFA':
        new_dfa = DFA()
        new_dfa.start = self.start.copy()
        for state in self.states:
            if state not in self.final:
                new_dfa.final.append(state)
            new_dfa.states.append(state)

        new_dfa.copyTransition(self)
        return new_dfa

    def union(self, dfa) -> 'DFA':
        from automata.NFA import NFA
        union_nfa = NFA()

        union_nfa.copyState(self)
        union_nfa.copyTransition(self)
        equiv_states = {}
        for state in dfa.states:
            equiv_states[state] = union_nfa.addState()

        for state in dfa.transitions:
            for literal in dfa.transitions[state]:
                for dest in dfa.transitions[state][literal]:
                    union_nfa.addTransition(equiv_states[state], equiv_states[dest], literal)

        start = union_nfa.addState()
        union_nfa.start = [start]
        union_nfa.addTransition(start, self.start[0], Automata.EPSILON)
        union_nfa.addTransition(start, equiv_states[dfa.start[0]], Automata.EPSILON)

        union_nfa.final += self.final
        for final_state in dfa.final:
            union_nfa.final.append(equiv_states[final_state])
        union_nfa.final += dfa.final

        union_nfa = union_nfa.removeEpsilon()
        return union_nfa.NFAtoDFA()

    def intersection(self, dfa):
        neg_dfa1 = self.negation()
        neg_dfa2 = dfa.negation()
        union = neg_dfa1.union(neg_dfa2)

        inter = union.negation()
        return inter


    def minimize(self):
        it = 0
        previous_equiv_classes = {}
        for notfinal_state in (set(self.states) - set(self.final)):
            previous_equiv_classes[notfinal_state] = it

        it += 1
        for final_state in self.final:
            previous_equiv_classes[final_state] = it


        finished = False
        new_equiv_classes = {}
        while not finished:
            new_equiv_classes = {}
            old_it = it
            for state1 in self.states:
                same = True
                for state2 in self.states:
                    if state1 == state2:
                        continue
                    if previous_equiv_classes[state1] != previous_equiv_classes[state2]:
                        continue
                    if state2 in new_equiv_classes:
                        continue
                    for label in range(Automata.ALPHABET_START, Automata.ALPHABET_END):
                        dest1 = self.transitions[state1][label][0]
                        dest2 = self.transitions[state2][label][0]
                        if previous_equiv_classes[dest1] != previous_equiv_classes[dest2]:
                            it += 1
                            new_equiv_classes[state2] = it
                            same = False
                            break
                if same:
                    new_equiv_classes[state1] = previous_equiv_classes [state1]

            if old_it == it:
                finished = True
            previous_equiv_classes = new_equiv_classes

        dfa = DFA()

        for state in self.states:
            new_state = previous_equiv_classes[state]
            dfa.states.append(new_state)

        for state in self.states:
            if state in self.transitions:
                for label in self.transitions[state]:
                    dest = self.transitions[state][label][0]
                    dfa.addTransition(new_equiv_classes[state], new_equiv_classes[dest], label)

        dfa.start = [new_equiv_classes[self.start[0]]]
        for final_state in self.final:
            if new_equiv_classes[final_state] not in dfa.final:
                dfa.final.append(new_equiv_classes[final_state])

        return dfa












