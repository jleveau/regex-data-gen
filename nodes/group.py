from nodes.node import Node

class Group(Node):
    def __init__(self, left):
        super().__init__("Group", [left])
