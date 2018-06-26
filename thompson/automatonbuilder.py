from automata import NFA
from automata.NFA import NFA
from automata.alphabet_iterator import Alphabet
from automata.automata import Automata
from nodes.concat import Concat
from nodes.group import Group
from nodes.literal import Literal
from nodes.node import Node
from nodes.star import Star
from nodes.union import Union


def union(nfa1: NFA, nfa2: NFA):
    nfa = NFA(Alphabet({Automata.EPSILON}))

    equiv_states = {}

    for state in nfa1.states:
        equiv_states[state] = nfa.addState()
    for state in nfa2.states:
        equiv_states[state] = nfa.addState()

    for state in nfa1.states:
        for label in nfa1.alphabet:
            for dest in nfa1.transitions[state][label]:
                nfa.addTransition(equiv_states[state], equiv_states[dest], label)

    for state in nfa2.states:
        for label in nfa2.alphabet:
            for dest in nfa2.transitions[state][label]:
                nfa.addTransition(equiv_states[state], equiv_states[dest], label)

    new_start = nfa.addState()
    new_end = nfa.addState()

    for start in nfa1.start:
        nfa.addTransition(new_start, equiv_states[start], NFA.EPSILON)
    for start in nfa2.start:
        nfa.addTransition(new_start, equiv_states[start], NFA.EPSILON)

    for final in nfa1.final:
        nfa.addTransition(equiv_states[final], new_end, NFA.EPSILON)
    for final in nfa2.final:
        nfa.addTransition(equiv_states[final], new_end, NFA.EPSILON)

    nfa.start = {new_start}
    nfa.final = {new_end}

    return nfa


def concat(nfa1: NFA, nfa2: NFA):

    nfa = NFA(Alphabet({Automata.EPSILON}))

    equiv_states = {}

    for state in nfa1.states:
        equiv_states[state] = nfa.addState()
    for state in nfa2.states:
        equiv_states[state] = nfa.addState()

    for start_state in nfa1.start:
        nfa.start.add(equiv_states[start_state])

    for final in nfa1.final:
        for start in nfa2.start:
            nfa.addTransition(equiv_states[final], equiv_states[start], NFA.EPSILON)

    for state in nfa1.states:
        for label in nfa.alphabet:
            for dest in nfa1.transitions[state][label]:
                nfa.addTransition(equiv_states[state], equiv_states[dest], label)

    for state in nfa2.states:
        for label in nfa.alphabet:
            for dest in nfa2.transitions[state][label]:
                nfa.addTransition(equiv_states[state], equiv_states[dest], label)

    for final in nfa2.final:
        nfa.final.add(equiv_states[final])
    return nfa


def star(nfa: NFA):
    new_start = nfa.addState()
    new_end = nfa.addState()

    for start in nfa.start:
        nfa.addTransition(new_start, start, NFA.EPSILON)
    for final in nfa.final:
        nfa.addTransition(final, new_end, NFA.EPSILON)
    for start in nfa.start:
        for final in nfa.final:
            nfa.addTransition(final, start, NFA.EPSILON)

    nfa.addTransition(new_start, new_end, NFA.EPSILON)
    nfa.start = [new_start]
    nfa.final = [new_end]
    return nfa



def literal(literal: Literal):
    nfa = NFA(Alphabet({Automata.EPSILON}))

    start = nfa.addState()
    final = nfa.addState()

    nfa.start = {start}
    nfa.final = {final}

    for label in literal.alphabet:
        for start in nfa.start:
            for final in nfa.final:
                nfa.addTransition(start, final, label)
    return nfa

def build(regextree: Node) -> NFA:
    if not regextree:
        return AutomatonBuilder.emptyWord()

    elif isinstance(regextree, Concat):
        nfa1 = build(regextree.getChildren()[0])
        nfa2 = build(regextree.getChildren()[1])
        return concat(nfa1, nfa2)

    elif isinstance(regextree, Union):
        nfa1 = build(regextree.getChildren()[0])
        nfa2 = build(regextree.getChildren()[1])
        return union(nfa1, nfa2)

    elif isinstance(regextree, Star):
        nfa = build(regextree.getChildren()[0])
        return star(nfa)

    elif isinstance(regextree, Literal):
        return literal(regextree)

    elif isinstance(regextree, Group):
        return build(regextree.getChildren()[0])

    else :
        raise Exception("Cannot build NFA for : :" + str(regextree))


class AutomatonBuilder:

    @staticmethod
    def toNFA(regextree: Node):
        if regextree == None:
            return AutomatonBuilder.emptyWord()
        nfa = build(regextree)
        nfa = nfa.removeEpsilon()

        return nfa

    @staticmethod
    def emptyWord():
        nfa = NFA(Alphabet())
        nfa.start = {nfa.addState()}
        nfa.final = nfa.start.copy()
        return nfa