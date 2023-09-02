from random import uniform


class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

        v1.edges.add(self)
        v2.edges.add(self)

    def get_relative(self, vertex):
        if vertex == v1:
            return v2
        if vertex == v2:
            return v1
        return None
