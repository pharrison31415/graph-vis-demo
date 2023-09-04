# graph-vis-demo

## Objective

This program is a proof of concept of a potentially bigger project for graph visualization.

Lots of types of data can be represented as graphs: social media following "maps", webpage linking, etc. This program aims to display graph information such that physical proximity helps indicate graphical adjacency to better visualize the data.

## Run

Run `main.py` with one system argument, the path to a graph data file.

eg: `$ python main.py data/big.txt`.

Toggle animation pause with the spacebar.

## Wikipedia Graph Data Generators

Both `wiki_crawl.py` and `wiki_circle.py` take one argument (Simple Wikipedia url path that comes after "/wiki/") generate graph data to stout.

`wiki_crawl.py` does a standard depth-first traversal (configurable in program) of a Simple Wikipedia page looking for other wikipedia page links after visiting the first page specified by the argument. Each new page is a new vertex. Each new link between any two pages is a new edge. This program generates a lot of "tangled" graphs with only 2 traversals; the following program produces less "tangled" graphs which are much prettier.

`wiki_circle.py` still demonstrates linkages between Simple Wikipedia pages. The vertices of the generated graph data are all the Simple Wikipedia pages linked directly from the first page specified by the argument. An edge between two vertices indicates that one of those Simple Wikipedia pages links directly to the other (directed graphs are not yet available).

eg: `$ python wiki_circle.py "Brigham_Young_University"`

## Graph Data Grammar

A file is split into two sections separated by a blank line. In the first section, each line is a unique identifier (uid) for a new vertex. In the second section, each line has two vertex uid's, separated by a space. See any file in the directory `data/`.
