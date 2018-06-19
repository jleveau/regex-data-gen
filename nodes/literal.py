from nodes.node import Node

digit = list("0123456789")
lower =  list("abcdefghijklmnopqrstuvwxyz")
upper =  list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alpha = lower + upper + digit
word =  lower + upper + ['_']
blank = list(" \t")
space = blank + list('\t\r\n\v\f')
punct = list('!"\#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~')

class Literal(Node):

    def __init__(self, alphabet):
        if isinstance(alphabet, list):
            self.alphabet = alphabet.copy()
        else:
            self.alphabet = [alphabet]
        super().__init__(self.alphabet, [])

    @staticmethod
    def fromAny() -> 'Literal':
        return Literal.fromRange(chr(0), chr(255))

    @staticmethod
    def fromRange(first, last) -> 'Literal':
        alphabet = []
        for i in range(ord(first), ord(last)+1):
            alphabet.append(str(chr(i)))
        return Literal(alphabet)

    @staticmethod
    def fromClass(classname) -> 'Literal':
        alphabet = []
        if classname == '[:digit:]':
            alphabet = list(digit)
        if classname =='[:lower:]':
            alphabet = list(lower)
        if classname ==  '[:upper:]':
            alphabet = list(upper)
        if classname == '[:alpha:]':
            alphabet = list(alpha)
        if classname == '[:word:]':
            alphabet = list(word)
        if classname == '[:blank:]':
            alphabet = list(blank)
        if classname == '[:space:]':
            alphabet = list(space)
        if classname == '[:punct:]':
            alphabet = list(punct)

        return Literal(alphabet)

    def __repr__(self):
        return "Literal: name"