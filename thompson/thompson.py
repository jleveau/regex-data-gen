from automata import automata
from automata.automata import NFA
from nodes.concat import Concat
from nodes.literal import Literal
from nodes.node import Node
from nodes.star import Star
from nodes.union import Union


def copyState(src :NFA, dest: NFA):
    for state in src.states:
        if not state in dest.states:
            dest.states.append(state)


def copyTransition(src: NFA, dest: NFA):
    for start in src.transitions.keys():
        for literal in src.transitions[start].keys():
            for final in src.transitions[start][literal]:
                dest.addTransition(start, final, literal)

def union(nfa1: NFA, nfa2: NFA):
    copyState(nfa2, nfa1)
    copyTransition(nfa2, nfa1)

    new_start = nfa1.addState()
    new_end = nfa1.addState()

    for start in nfa1.start:
        nfa1.addTransition(new_start, start, NFA.EPSILON)
    for start in nfa2.start:
        nfa1.addTransition(new_start, start, NFA.EPSILON)

    for final in nfa1.final:
        nfa1.addTransition(final, new_end, NFA.EPSILON)
    for final in nfa2.final:
        nfa1.addTransition(final, new_end, NFA.EPSILON)


    nfa1.start = [new_start]
    nfa1.final = [new_end]

    return nfa1


def concat(nfa1: NFA, nfa2: NFA):
    copyState(nfa2, nfa1)
    copyTransition(nfa2, nfa1)

    for final in nfa1.final :
        for start in nfa2.start:
            nfa1.addTransition(final, start, NFA.EPSILON)

    nfa1.final = nfa2.final
    return nfa1

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
    nfa = NFA()
    state = nfa.addState()
    nfa.addTransition(nfa.final[0], state, literal.name)
    nfa.final = [state]
    return nfa

def frontClosure(nfa: NFA, label, src, dest):
    if not dest in nfa.transitions:
        return
    if not NFA.EPSILON in nfa.transitions[dest]:
        return

    for dest_epsilon in nfa.transitions[dest][NFA.EPSILON]:
        nfa.addTransition(src, dest_epsilon, label)
        frontClosure(nfa, label, src, dest_epsilon)

    for state in nfa.states:
        if not state in nfa.transitions.keys():
            nfa.states.remove(state)

def removeEpsilon(nfa: NFA):

    for state in nfa.transitions.keys():
        for literal in nfa.transitions[state]:
            if not literal == NFA.EPSILON:
                for dest in nfa.transitions[state][literal]:
                    frontClosure(nfa, literal, state, dest)

    for state in nfa.transitions.keys():
        nfa.transitions[state][NFA.EPSILON] = []

    return nfa

def build(regextree: Node) -> NFA:

    if not regextree:
        return Thompson.emptyWord()

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

    else :
        raise "Cannot build NFA for : " + str(regextree)

class Thompson:

    @staticmethod
    def toNFA(regextree: Node):
        if regextree == None:
            return Thompson.emptyWord()
        nfa = build(regextree)
        nfa = removeEpsilon(nfa)
        return nfa

    @staticmethod
    def emptyWord():
        nfa = NFA()
        return nfa