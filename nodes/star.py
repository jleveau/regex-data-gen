from nodes.node import Node


class Star(Node):
    def __init__(self, left):
        super().__init__("Star", [left])
