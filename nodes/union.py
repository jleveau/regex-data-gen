from nodes.node import Node


class Union(Node):
    def __init__(self, left, right):
        super().__init__("Union", [left, right])


