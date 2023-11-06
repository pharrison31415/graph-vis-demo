import sys
import requests
from random import uniform
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def wiki_links_from(page):
    response = requests.get(f"https://simple.wikipedia.org/wiki/{page}")
    # response = requests.get(f"https://en.wikipedia.org/wiki/{page}")
    soup = BeautifulSoup(response.content, features="html.parser")

    return soup.find_all("a")


def startswith_stupid(href):
    stupid = ["Category", "File", "Help", "Portal",
              "Special", "Talk", "Template", "Template_talk", "Wikipedia"]
    if href.startswith("/wiki/Main_Page"):
        return True
    for s in stupid:
        if href.startswith(f"/wiki/{s}:"):
            return True

    return False


def main():
    origin = sys.argv[1]
    vertices = set()
    edges = set()

    for a in wiki_links_from(origin):
        href = a.get("href")
        if href is not None \
                and href.startswith("/wiki/") \
                and href != f"/wiki/{origin}" \
                and not startswith_stupid(href):
            destination = href[6:]
            vertices.add(destination)

    for vertex in vertices:
        for a in wiki_links_from(vertex):
            href = a.get("href")
            if href is not None:
                destination = href[6:]
                if destination != vertex and destination in vertices:
                    edges.add(f"{vertex} {destination}")

    for vertex in vertices:
        print(vertex)

    print()

    for edge in edges:
        print(edge)


if __name__ == "__main__":
    main()
