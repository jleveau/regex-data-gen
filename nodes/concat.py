from nodes.node import Node


class Concat(Node):
    def __init__(self, left, right):
        super().__init__("Concat", [left, right])
