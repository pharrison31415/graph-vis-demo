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

    vertices = {}
    edges = set()

    with open(sys.argv[1]) as data:
        for line in data:
            uid = line.strip()
            if uid == "":
                break
            new_vert = Vertex(uid)
            vertices[uid] = new_vert

        for line in data:
            uid1, uid2 = line.strip().split(" ")
            v1, v2 = vertices[uid1], vertices[uid2]
            new_edge = Edge(v1, v2)
            edges.add(new_edge)

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
            for v1 in vertices.values():
                v1.ddx = 0
                v1.ddy = 0
                for v2 in vertices.values():
                    if v1 == v2:
                        continue

                    repel_x, repel_y = v1.repel(v2)
                    spring_x, spring_y = v1.spring(v2)
                    v1.ddx += repel_x + spring_x
                    v1.ddy += repel_y + spring_y

        # update vertex positions
        for vertex in vertices.values():
            if not paused:
                vertex.update_pos()

        # draw edges
        for edge in edges:
            pygame.draw.line(surface, (255, 255, 255),
                             (edge.v1.x, edge.v1.y), (edge.v2.x, edge.v2.y))

        # draw vertices
        for vertex in vertices.values():
            pygame.draw.circle(surface, (255, 0, 0),
                               (vertex.x, vertex.y), vertex.radius)

        pygame.display.update()


if __name__ == "__main__":
    main()
