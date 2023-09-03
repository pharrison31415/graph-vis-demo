import pygame
import sys

from Vertex import Vertex
from Edge import Edge


def gravity(r): return -1/(r**2)
def repel(r): return 1/(r**3)


# WIDTH, HEIGHT = 1200, 600
WIDTH, HEIGHT = 600, 600


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("graph-vis-demo")

    Vertex.WIDTH = WIDTH
    Vertex.HEIGHT = HEIGHT
    Vertex.TEMP = 1

    a = Vertex()
    b = Vertex()
    c = Vertex()
    vertices = [a, b, c]

    ab = Edge(a, b)
    ac = Edge(a, c)
    edges = [ab, ac]

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                sys.exit()
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                print([(v.ax, v.ay) for v in vertices])

        # update vertex accelerations
        for v1 in vertices:
            v1.ax, v1.ay = 0, 0
            for v2 in vertices:
                if v1 == v2:
                    continue

                repel_x, repel_y = v1.repel(v2)
                v1.ax += repel_x
                v2.ay += repel_y

        # update vertex positions and draw
        for vertex in vertices:
            vertex.update_pos()
            pygame.draw.circle(surface, (255, 255, 255),
                               (vertex.x, vertex.y), vertex.radius)

        # draw edges
        for edge in edges:
            pygame.draw.line(surface, (255, 255, 255),
                             (edge.v1.x, edge.v1.y), (edge.v2.x, edge.v2.y))

        pygame.display.update()


if __name__ == "__main__":
    main()
