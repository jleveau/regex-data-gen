from automata.DFA import DFA
from automata.alphabet_iterator import Alphabet
from automata.automata import Automata

def getEpsilonReachable(nfa, start):
    visited, stack = set(), [start]
    reachable = set()
    while stack:
        current = stack.pop()
        reachable.add(current)
        if current not in visited:
            visited.add(current)
            next = set()
            if current in nfa.transitions and NFA.EPSILON in nfa.transitions[current]:
                next = nfa.transitions[current][NFA.EPSILON]
            stack.extend(next - visited)
    return reachable


class NFA(Automata):

    def __init__(self, alphabet):
        super().__init__(alphabet)

    def NFAtoDFA(self):
        dfa = DFA(Alphabet())
        src = tuple(self.start)

        start = src
        powerset = {src: {}}

        group_state_list = [src]
        it = 0

        while it < len(group_state_list):
            src = group_state_list[it]
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
                if len(dest) > 0 and dest not in powerset:
                    powerset[dest] = {}
                    group_state_list.append(dest)
            it += 1

        state_names = {}
        for state in powerset:
            state_names[state] = dfa.addState()

        for state in powerset:
            for label in powerset[state]:
                if powerset[state][label] not in state_names:
                    state_names[powerset[state][label]] = dfa.addState()

                dfa.addTransition(state_names[state], state_names[powerset[state][label]], label)

        dfa.start = [state_names[start]]

        for state in powerset:
            for sub_state in state:
                if sub_state in self.final and state_names[state] not in dfa.final:
                    dfa.final.add(state_names[state])
                    break

        for final_state in self.final:
            for state in powerset:
                if final_state in state:
                    dfa.final.add(state_names[state])

        for state_name in state_names:
            if len(state_name) == 0:
                for literal in self.alphabet:
                    dfa.addTransition(state_names[state_name], state_names[state_name], literal)
                break
        return dfa

    def removeEpsilon(self) -> 'NFA':

        new_nfa = NFA(Alphabet())

        equiv_states = {}
        for state in self.states:
            equiv_states[state] = new_nfa.addState()

        epsilon_reachable = {}
        for state_src in self.states:
            epsilon_reachable[state_src] = getEpsilonReachable(self, state_src)

        for start in self.start:
            for state in epsilon_reachable[start]:
                new_nfa.start.add(equiv_states[state])

        for state in self.states:
            for final_state in self.final:
                if final_state in epsilon_reachable[state]:
                    new_nfa.final.add(equiv_states[state])

        for state in self.states:
            for label in self.alphabet.letters - {Automata.EPSILON}:
                for dest in self.transitions[state][label]:
                    new_nfa.addTransition(equiv_states[state], equiv_states[dest], label)

        for state_src in self.states:
            for label in self.alphabet.letters - {Automata.EPSILON}:
                for dest in self.transitions[state_src][label]:
                    for reachable in epsilon_reachable[dest]:
                        new_nfa.addTransition(equiv_states[state_src], equiv_states[reachable], label)

        return new_nfa
