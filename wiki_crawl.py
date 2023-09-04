import sys
import requests
from random import uniform
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def crawl(origin, depth, vertices, edges, chance):
    if depth == 0:
        return

    response = requests.get(f"https://simple.wikipedia.org/wiki/{origin}")
    soup = BeautifulSoup(response.content, features="html.parser")

    for a in soup.find_all("a"):
        href = a.get("href")
        if href is None or not href.startswith("/wiki/"):
            continue

        destination = href[6:]
        vertices.add(destination)
        edges.add(f"{origin} {destination}")

        crawl(destination, depth-1, vertices, edges, 1)


def main():
    origin = sys.argv[1]
    depth = 1

    vertices = {origin}
    edges = set()

    crawl(origin, depth, vertices, edges, 1)

    # trim out vertices with one edge
    # vertices_to_remove = set()
    # for vertex in vertices:
    #     edge_count = 0
    #     edges_to_remove = set()
    #     for edge in edges:
    #         if vertex in edge:
    #             edge_count += 1
    #             edges_to_remove.add(edge)

    #     if edge_count < 2:
    #         vertices_to_remove.add(vertex)
    #         for edge in edges_to_remove:
    #             edges.remove(edge)

    # for vertex in vertices_to_remove:
    #     vertices.remove(vertex)

    for vertex in vertices:
        print(vertex)

    print()

    for edge in edges:
        print(edge)


if __name__ == "__main__":
    main()
