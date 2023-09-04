# graph-vis-demo

## Objective

This program is a proof of concept of a potentially bigger project for graph visualization.

Lots of types of data can be represented as graphs: social media following "maps", webpage linking, etc. This program aims to display graph information such that physical proximity helps indicate graphical adjacency to better visualize the data.

## Run

Run `main.py` with one system argument, the path to a graph data file.
eg:
`$ python main.py data/big.txt`. Toggle animation pause with the spacebar.

## Graph Data Grammar

The file is split into two sections separated by a blank line. In the first section, each line is a unique identifier (uid) for a new vertex. In the second section, each line has two vertex uid's, separated by a space. See `data/big.txt`.
