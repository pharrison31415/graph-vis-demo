import pygame
import sys

from Vertex import Vertex
from Edge import Edge

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
    d = Vertex()
    vertices = [a, b, c, d]

    ab = Edge(a, b)
    ac = Edge(a, c)
    bc = Edge(b, c)
    bd = Edge(b, d)
    cd = Edge(c, d)
    edges = [ab, ac, bc, bd, cd]

    paused = False
    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                sys.exit()
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                paused = not paused

        # update vertex accelerations
        if not paused:
            for v1 in vertices:
                for v2 in vertices:
                    if v1 == v2:
                        continue

                    repel_x, repel_y = v1.repel(v2)
                    spring_x, spring_y = v1.spring(v2)
                    v1.ddx += repel_x + spring_x
                    v2.ddy += repel_y + spring_y

        # update vertex positions and draw
        for vertex in vertices:
            if not paused:
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
