from random import uniform


class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

        v1.edges.add(v2)
        v2.edges.add(v1)
