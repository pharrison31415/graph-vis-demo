from random import uniform


class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

        v1.edges.add(self)
        v2.edges.add(self)

    def get_relative(self, vertex):
        if vertex == self.v1:
            return self.v2
        if vertex == self.v2:
            return self.v1
        return None
