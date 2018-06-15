from automata import NFA
from automata.NFA import NFA
from nodes.concat import Concat
from nodes.group import Group
from nodes.literal import Literal
from nodes.node import Node
from nodes.star import Star
from nodes.union import Union


def union(nfa1: NFA, nfa2: NFA):
    nfa1.copyState(nfa2)
    nfa1.copyTransition(nfa2)

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
    nfa1.copyState(nfa2)
    nfa1.copyTransition(nfa2)

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

    start = nfa.addState()
    final = nfa.addState()

    nfa.start = [start]
    nfa.final = [final]

    nfa.addTransition(nfa.start[0], nfa.final[0], ord(literal.name))
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

    elif isinstance(regextree, Group):
        return build(regextree.getChildren()[0])

    else :
        raise "Cannot build NFA for : " + str(regextree)


class Thompson:

    @staticmethod
    def toNFA(regextree: Node):
        if regextree == None:
            return Thompson.emptyWord()
        nfa = build(regextree)
        nfa = nfa.removeEpsilon()
        return nfa

    @staticmethod
    def emptyWord():
        nfa = NFA()
        return nfa