from automata import Automaton
from automata.Automaton import Automaton
from nodes.concat import Concat
from nodes.literal import Literal
from nodes.node import Node
from nodes.star import Star
from nodes.union import Union


def copyState(src :Automaton, dest: Automaton):
    for state in src.states:
        if not state in dest.states:
            dest.states.append(state)


def copyTransition(src: Automaton, dest: Automaton):
    for start in src.transitions.keys():
        for literal in src.transitions[start].keys():
            for final in src.transitions[start][literal]:
                dest.addTransition(start, final, literal)

def union(nfa1: Automaton, nfa2: Automaton):
    copyState(nfa2, nfa1)
    copyTransition(nfa2, nfa1)

    new_start = nfa1.addState()
    new_end = nfa1.addState()

    for start in nfa1.start:
        nfa1.addTransition(new_start, start, Automaton.EPSILON)
    for start in nfa2.start:
        nfa1.addTransition(new_start, start, Automaton.EPSILON)

    for final in nfa1.final:
        nfa1.addTransition(final, new_end, Automaton.EPSILON)
    for final in nfa2.final:
        nfa1.addTransition(final, new_end, Automaton.EPSILON)


    nfa1.start = [new_start]
    nfa1.final = [new_end]

    return nfa1


def concat(nfa1: Automaton, nfa2: Automaton):
    copyState(nfa2, nfa1)
    copyTransition(nfa2, nfa1)

    for final in nfa1.final :
        for start in nfa2.start:
            nfa1.addTransition(final, start, Automaton.EPSILON)

    nfa1.final = nfa2.final
    return nfa1

def star(nfa: Automaton):
    new_start = nfa.addState()
    new_end = nfa.addState()

    for start in nfa.start:
        nfa.addTransition(new_start, start, Automaton.EPSILON)
    for final in nfa.final:
        nfa.addTransition(final, new_end, Automaton.EPSILON)
    for start in nfa.start:
        for final in nfa.final:
            nfa.addTransition(final, start, Automaton.EPSILON)

    nfa.addTransition(new_start, new_end, Automaton.EPSILON)
    nfa.start = [new_start]
    nfa.final = [new_end]
    return nfa



def literal(literal: Literal):
    nfa = Automaton()
    state = nfa.addState()
    nfa.addTransition(nfa.final[0], state, literal.name)
    nfa.final = [state]
    return nfa

def hasEpsilonPathRec(nfa, current, dest, visited):
    if current in visited:
        return False
    visited.append(current)
    if current == dest:
        return True
    if not current in nfa.transitions:
        return False
    if not Automaton.EPSILON in nfa.transitions[current]:
        return False

    for state in nfa.transitions[current][Automaton.EPSILON]:
        if not state in visited:
            if hasEpsilonPathRec(nfa, state, dest, visited):
                return True
    return False

def hasEpsilonPath(nfa, src, dest):
    return hasEpsilonPathRec(nfa, src, dest, [])

def hasPathFromStartRec(nfa, target ,current, visited):
    if current in visited:
        return False
    visited.append(current)
    if current == target:
        return True
    if not current in nfa.transitions:
        return False

    for label in nfa.transitions[current]:
        for dest in nfa.transitions[current][label]:
            return hasPathFromStartRec(nfa, target, dest, visited)


def hasPathFromStart(nfa, state):
    if state in nfa.start:
        return True
    for start in nfa.start:
        if hasPathFromStartRec(nfa, state, start, []):
            return True
    return False


def removeEpsilon(nfa: Automaton):

    new_nfa = Automaton()
    new_nfa.states = []
    new_nfa.start = []
    new_nfa.final = []
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

    #front closure
    for state_src in nfa.states:
        for state_dest in nfa.states:
            if state_dest != state_src and hasEpsilonPath(nfa, state_src, state_dest) and state_dest in nfa.transitions:
                for literal in nfa.transitions[state_dest]:
                    if literal != Automaton.EPSILON:
                        for epsilon_dest in nfa.transitions[state_dest][literal]:
                            new_nfa.addTransition(state_src, epsilon_dest, literal)

    to_remove = set()
    #Remove unreachable states
    for state in new_nfa.states:
        if not hasPathFromStart(new_nfa, state):
            if state in new_nfa.transitions:
                new_nfa.transitions.pop(state)
            to_remove.add(state)

    #remove not final states with no transition
    for state in new_nfa.states:
        if not state in new_nfa.transitions and not state in new_nfa.final:
            to_remove.add(state)

    for state in to_remove:
        if state in new_nfa.transitions:
            new_nfa.transitions.pop(state)
        if state in new_nfa.start:
            new_nfa.start.remove(state)
        if state in new_nfa.final:
            new_nfa.final.remove(state)
        new_nfa.states.remove(state)

    return new_nfa

def build(regextree: Node) -> Automaton:

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
        nfa = Automaton()
        return nfa