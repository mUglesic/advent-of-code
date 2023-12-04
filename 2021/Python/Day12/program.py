
import sys

def create_graph(data):

    g = Graph()

    for line in data:
        for node in line:
            g.add(Node(node))

    for line in data:
        g.connect(line[0], line[1])

    g.start = g.find("start")
    g.end = g.find("end")

    return g

def find_paths(g):

    return find_path(g.start, [])

def find_path(node, visited):

    if node in visited and not node.big:
        return 0

    visited.append(node)

    if node == "end":
        # print("PATH")
        # print([el.name for el in visited])
        return 1

    s = 0

    for n in node.conns:

        s += find_path(n, list(visited))

    return s


def main():

    data = []

    with open(sys.argv[1]) as f:
        for line in f:
            data.append(line.strip().split("-"))

    g = create_graph(data)

    print(g)

    print("Part One: {}".format(find_paths(g)))

################################################

class Graph:

    def __init__(self):
        self.start = None
        self.end = None
        self.nodes = []

    def add(self, node):
        if node in self.nodes:
            return False
        self.nodes.append(node)
        return True

    def find(self, node):
        for n in self.nodes:
            if n == node:
                return n

    def connect(self, node1, node2):

        n1 = self.find(node1)
        n2 = self.find(node2)

        n1.connect(n2)
        n2.connect(n1)

    def __str__(self):
        return "\n".join(map(str, self.nodes))

class Node:

    def __init__(self, name):
        self.name = name
        self.big = name.isupper()
        self.conns = []

    def connect(self, node):
        if node not in self.conns:
            self.conns.append(node)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other
        return False

    def __str__(self):
        return "{} | Connections: {}".format(self.name, ", ".join([con.name for con in self.conns]))

if __name__ == "__main__":
    main()