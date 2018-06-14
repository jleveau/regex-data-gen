from nodes.node import Node


class Literal(Node):
    def __init__(self, name):
        super().__init__(name, [])

    def __repr__(self):
        return "Literal: name"