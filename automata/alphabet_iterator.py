

class Alphabet:

    def __init__(self, additionnal_letters=set()):
        self.letters = set()
        for i in range(256):
            self.letters.add(chr(i))
        self.letters = self.letters.union(additionnal_letters)

    def __iter__(self):
        return list(self.letters).__iter__()
