from automata.automata import Automata


class Alphabet:

    alphabet = []
    def __init__(self):
        self.i = 0
        self.n = len(Alphabet.alphabet)

    def __iter__(self):
        return self

    def __next__ (self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

    @staticmethod
    def isInAlphabet(literal):
        return literal in Alphabet.alphabet

    @staticmethod
    def addToAlphabet(l):
        Alphabet.alphabet.append(l)