# Project description
## Goal: 
For a list of Australian cities obtain a minimal spanning tree (in the graph the weight of an edge is assumed to be Eucledian distance between the cities it connects), using Kruskal, Prim & Boruvka algorithms. Visualise the tree, compare obtained distances with existing.
## Used technlogies: 
Python 3.7, Folium, Google API

# Data:
List of cities was obtained from Britannica
For the list via Google API a .csv file of coordinates was made
For futher work with Folium the .csv file was converted into .txt, which then was used in inputfix.txt to obtain an array of cities. The cities are represented as arrays [name, latitude, longitude].

# Code:
**main.py**
### Node structure:
a node is implemented as an object of class Node with attributes ‘name’ (string), ‘rank’ (integer), ‘long’ (longitude, float) and ‘lat’ (latitude, float).
### Graph structure: 
a graph is implemented as an object of class Graph with attributed ‘graph’ (array of edges), ‘nodes’ (array of nodes) and ‘parent’ (dictionary with nodes as keys and the root of the tree a node currently belongs to as value for any key). Methods are addNode(name, latitude, longitude), find(node) (finds the root of the tree the node belongs to), connect(u, v) (connect the connected components the nodes belong to)
### Function makeGraph(file.csv):
makes an object of type Graph from the given .csv file of nodes

## Algorithms:
### Kruskal:
A set ‘MST’ is created to store the resulting tree. The list of edges is sorted by weight in the acsending order. A cycle runs through the list, for each edge checking if the edge is 
### Prim: 
First, we create an empty set ‘MST’ and an additional list ‘X’ to store our edges. Starting with an arbitrary node, we add nodes into our ‘X’ list step by step, and then run the following procedures until the number of elements in ‘X’ equals a total number of nodes in our graph. At each iteration of a cycle, we create a list of edges we are choosing from on this particular step. Then, for each node, already added to our ‘X’ list, we look at the edges between it and the neighbor node, create a list of all edges between the initial one and neighbors, choose the one with lower weight, and add it to the MST. Then, add a new node (to which we have a path already) to the ‘X’ list, and repeat the iteration.
### Boruvka:

### Function equal(set, set):
compares two sets of edges. Needed because default sets comparison does not count edges (a, b, weight) and (b, a, weight) as equal, which they are, as 


## Drive part: 
### Finding MST (minimal spanning tree): 
First, a graph g is made from given data, then all three algorithms are runned on it, obtained trees are stored as ansK (for Kruskal), ansB (for Boruvka) and ansP (for Prim). All three are compared, and, if all three are equal, which implies that the algorithms are imolemented correctly, line ‘found MST’ is printed out.
### Output (Map Description): 
We imported folium library to create a map. From the Kruskal algorithm, we had a set of all edges in MST. This set consists of tuples, in each tuple there are three objects: start node, finish node, weight. Firstly, we construct markers with coordinates of the cities, using built-in methods of folio library. Secondly, we connect those markers. Coordinates of markers are taken from the properties of the nodes.

# Result: 
the obtained MST is visualised on a map via Folium library. Also a comparison table is constructed in a form of a .csv file
