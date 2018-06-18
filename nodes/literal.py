from nodes.node import Node

digit = "0123456789"
lower =  "abcdefghijklmnopqrstuvwxyz"
upper =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = lower + upper + digit
word =  lower + upper + '_'
blank = " \t"
space = blank + '\t\r\n\v\f'
punct = '!"\#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~'


class Literal(Node):
    def __init__(self, alphabet):
        if isinstance(alphabet, list):
            self.alphabet = alphabet.copy()
        else:
            self.alphabet = [alphabet]
        super().__init__(self.alphabet, [])

    @staticmethod
    def fromRange(first, last) -> 'Literal':
        alphabet = []
        for i in range(first, last+1):
            alphabet.append(chr(i))
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