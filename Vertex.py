from random import uniform


class Vertex:
    WIDTH, HEIGHT = 1200, 600
    TEMP = 0

    def __init__(self):
        self.x = uniform(0, Vertex.WIDTH)
        self.y = uniform(0, Vertex.HEIGHT)
        self.dx = 0
        self.dy = 0
        self.ax = 0
        self.ay = 0

        self.radius = 4

        self.edges = set()

    def update_pos(self, dt=0.01):
        self.dx += self.ax*dt
        self.dy += self.ay*dt

        self.x += self.dx*dt + uniform(-Vertex.TEMP, Vertex.TEMP)
        self.y += self.dy*dt + uniform(-Vertex.TEMP, Vertex.TEMP)

        if self.x < self.radius:
            self.x = self.radius
            self.dx = 0
        if self.x > Vertex.WIDTH-self.radius:
            self.x = Vertex.WIDTH-self.radius
            self.dx = 0
        if self.y < self.radius:
            self.y = self.radius
            self.dy = 0
        if self.y > Vertex.HEIGHT-self.radius:
            self.y = Vertex.HEIGHT-self.radius
            self.dy = 0
