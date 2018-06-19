

class Alphabet:

    def __init__(self):
        self.letters = set()
        for i in range(256):
            self.letters.add(chr(i))

    def __iter__(self):
        return list(self.letters).__iter__()

    def next(self):
        return list(self.letters).next()

    def isInAlphabet(self, literal):
        return literal in self.letters

    def addToAlphabet(self, l):
        self.letters.add(l)

    def mergeAlphabet(self, alphabet):
        for l in alphabet:
            self.letters.add(l)

    def interAlphabet(self, alphabet):
        return self.letters.intersection(alphabet)