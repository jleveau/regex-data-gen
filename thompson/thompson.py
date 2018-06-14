from automata import NFA
from automata.NFA import NFA
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

def hasEpsilonPathRec(nfa, current, dest, visited):
    visited.append(current)
    if current == dest:
        return True
    if not current in nfa.transitions:
        return False
    if not NFA.EPSILON in nfa.transitions[current]:
        return False

    for state in nfa.transitions[current][NFA.EPSILON]:
        if not state in visited:
            if hasEpsilonPathRec(nfa, state, dest, visited):
                return True
    return False

def hasEpsilonPath(nfa, src, dest):
    return hasEpsilonPathRec(nfa, src, dest, [])

def hasPathFromStartRec(nfa, state, current, visited):
    visited.append(current)
    if current in nfa.start:
        return True
    if not current in nfa.transitions:
        return False


def hasPathFromStart(nfa, state):
    for start in nfa.start:
        if hasPathFromStartRec(nfa, state, state, []):
            return True
    return False


def removeEpsilon(nfa: NFA):

    new_nfa = NFA()
    new_nfa.states = []
    new_nfa.start = []
    new_nfa.end = []
    new_nfa.transitions = {}
    new_nfa.alphabet = nfa.alphabet.copy()

    copyState(nfa, new_nfa)

    for start in nfa.start:
        if start in nfa.transitions:
            for state in nfa.states:
                if hasEpsilonPath(nfa, start, state):
                    new_nfa.start.append(state)

    for state in nfa.states:
        for final_state in nfa.final:
            if hasEpsilonPath(nfa, state, final_state):
                new_nfa.final.append(state)


    for state_src in nfa.states:
        for state_dest in nfa.states:
            if state_dest != state_src:
                if hasEpsilonPath(nfa, state_src, state_dest):
                    for state_epsilon_dest in nfa.states:
                        if hasEpsilonPath(nfa, state_dest, state_epsilon_dest):
                            if state_dest in nfa.transitions:
                                for literal in nfa.transitions[state_dest]:
                                    if literal != NFA.EPSILON:
                                        for epsilon_dest in nfa.transitions[state_dest][literal]:
                                            new_nfa.addTransition(state_src, epsilon_dest, literal)


    for state in new_nfa.states:
        if not state in new_nfa.transitions:
            new_nfa.states.remove(state)
    return new_nfa

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