from typing import List

it = 0

class Node:

    def __init__(self, name, children):
        global it
        self.name = name
        self.id = it
        it += 1
        self.children = children

    __init__.it = 0

    def getChildren(self) -> List['Node']:
        return self.children

    def toDot(self):
        graph = {}
        graph["transitions"] = ""
        graph["nodes"] = ""

        nodeToDot(self, graph)
        return "digraph G { \n" + graph["transitions"] + graph["nodes"] + "\n}"


def nodeToDot(node, graph):
    graph["nodes"] += "\t" + str(node.id) + ' [label= "' + node.name + '"] ' + ';\n'
    for child in node.children:
        graph["transitions"] += "\t" + str(node.id) + " -> " + str(child.id) + ";\n"
        nodeToDot(child, graph)
