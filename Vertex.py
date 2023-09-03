from random import uniform
from math import sqrt


class Vertex:
    WIDTH, HEIGHT = 1200, 600
    MAX_VEL = 0.5
    TEMP = 0
    REPEL = 1

    def __init__(self):
        self.x = uniform(0, Vertex.WIDTH)
        self.y = uniform(0, Vertex.HEIGHT)
        self.dx = 0
        self.dy = 0
        self.ddx = 0
        self.ddy = 0

        self.m = 1

        self.radius = 6

        self.edges = set()

    def repel(self, vertex):
        delta_x = self.x - vertex.x
        delta_y = self.y - vertex.y

        # divibe by zero
        if (delta_x, delta_y) == (0, 0):
            return (0, 0)

        dist = sqrt(delta_x**2 + delta_y**2)
        magnitude = Vertex.REPEL * self.m * vertex.m / dist**2

        return [magnitude * delta_x/dist, -magnitude * delta_y/dist]

    def update_pos(self, dt=1):
        # update velocity
        self.dx += self.ddx*dt
        self.dy += self.ddy*dt

        # modify velocity
        if self.dx > Vertex.MAX_VEL:
            self.dx = Vertex.MAX_VEL
            self.ddx = 0
        if self.dx < -Vertex.MAX_VEL:
            self.dx = -Vertex.MAX_VEL
            self.ddx = 0
        if self.dy > Vertex.MAX_VEL:
            self.dy = Vertex.MAX_VEL
            self.ddy = 0
        if self.dy < -Vertex.MAX_VEL:
            self.dy = -Vertex.MAX_VEL
            self.ddy = 0

        # update position
        self.x += self.dx*dt + uniform(-Vertex.TEMP, Vertex.TEMP)
        self.y += self.dy*dt + uniform(-Vertex.TEMP, Vertex.TEMP)

        # modify position
        if self.x < self.radius:
            self.x = self.radius
            self.dx = 0
            self.ddx = 0
        if self.x > Vertex.WIDTH-self.radius:
            self.x = Vertex.WIDTH-self.radius
            self.dx = 0
            self.ddx = 0
        if self.y < self.radius:
            self.y = self.radius
            self.dy = 0
            self.ddy = 0
        if self.y > Vertex.HEIGHT-self.radius:
            self.y = Vertex.HEIGHT-self.radius
            self.dy = 0
            self.ddy = 0
