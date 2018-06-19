from automata.DFA import DFA
from automata.automata import Automata


def hasEpsilonPath(nfa, src, dest):
    return hasEpsilonPathRec(nfa, src, dest, [])


def hasEpsilonPathRec(nfa, current, dest, visited):
    if current in visited:
        return False
    visited.append(current)
    if current == dest:
        return True

    if current not in nfa.transitions or NFA.EPSILON not in nfa.transitions[current]:
        return False

    for state in nfa.transitions[current][NFA.EPSILON]:
        if state not in visited:
            if hasEpsilonPathRec(nfa, state, dest, visited):
                return True
    return False


class NFA(Automata):

    def __init__(self):
        super().__init__()

    def NFAtoDFA(self):
        dfa = DFA()

        self.start.sort()
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
                    dfa.final.append(state_names[state])
                    break

        for final_state in self.final:
            for state in powerset:
                if final_state in state:
                    dfa.final.append(state_names[state])

        for state_name in state_names:
            if len(state_name) == 0:
                for literal in self.alphabet:
                    dfa.addTransition(state_names[state_name], state_names[state_name], literal)
                break

        dfa.removeUnReachableState()

        return dfa

    def removeEpsilon(self) -> 'NFA':

        new_nfa = NFA()
        new_nfa.copyState(self)

        for start in self.start:
            if start in self.transitions:
                for state in self.states:
                    if hasEpsilonPath(self, start, state):
                        new_nfa.start.append(state)

        for state in self.states:
            for final_state in self.final:
                if hasEpsilonPath(self, state, final_state):
                    new_nfa.final.append(state)

        for state in self.states:
            if state in self.transitions :
                for label in self.transitions[state]:
                    if label != NFA.EPSILON:
                        for dest in self.transitions[state][label]:
                            new_nfa.addTransition(state, dest, label)

        for state_src in self.states:
            for state_dest in self.states:
                if state_dest != state_src \
                        and hasEpsilonPath(self, state_src, state_dest) \
                        and state_dest in self.transitions:
                    for literal in self.transitions[state_dest]:
                        if literal != NFA.EPSILON:
                            for epsilon_dest in self.transitions[state_dest][literal]:
                                new_nfa.addTransition(state_src, epsilon_dest, literal)

        new_nfa.removeUnReachableState()

        return new_nfa
