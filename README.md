# Project description
## Goal: 
For a list of Australian cities obtain a minimal spanning tree (in the graph the weight of an edge is assumed to be Eucledian distance between the cities it connects), using Kruskal, Prim & Boruvka algorithms. Visualise the tree, compare obtained distances with existing.
## Used technlogies: 
Python 3.7, Folium, Google API

# Data:
List of cities was obtained from Britannica
For the list via Google API a .csv file of coordinates was made
For futher work with Folium the .csv file was converted into .txt, which then was used in inputfix.txt to obtain an array of cities. The cities are represented as arrays [name, latitude, longitude].
As we have already assumed we work on a plane, not a globe, we have decided to use a scale of 1 deg = 100 km (since for any part of the globe 1 deg of latitude is equal to 111 km and for longitude the scale changes depending on the latitude, so we picked the scale on 26 deg south latitude, which is the central latitude of Australia, and where the value is around 100 km per degree)

# Code:
**main.py**
### Node structure:
A node is implemented as an object of class Node with attributes ‘name’ (string), ‘rank’ (integer), ‘long’ (longitude, float) and ‘lat’ (latitude, float).
### Graph structure: 
A graph is implemented as an object of class Graph with attributed ‘graph’ (array of edges), ‘nodes’ (array of nodes) and ‘parent’ (dictionary with nodes as keys and the root of the tree a node currently belongs to as value for any key). Methods are addNode(name, latitude, longitude), find(node) (finds the root of the tree the node belongs to), connect(u, v) (connect the connected components the nodes belong to)
### Function makeGraph(file.csv):
Makes an object of type Graph from the given .csv file of nodes
### Function equal(set, set):
Compares two sets of edges. Needed because default sets comparison does not count edges (a, b, weight) and (b, a, weight) as equal, which they are, as the graph we work with is undirected. Through two cycles it checks that all the edges from set 1 are in set 2 and edges from set 2 are in set 1, so that they are equal.

## Algorithms:
### Kruskal:
A set ‘MST’ is created to store the resulting tree. The list of edges is sorted by weight in the acsending order. A cycle runs through the list, for each edge checking if the addition of this edge causes a cycle in MST. If not, we add the edge, else we discard it. 
### Prim: 
First, we create an empty set ‘MST’ and an additional list ‘X’ to store our edges. Starting with an arbitrary node, we add nodes into our ‘X’ list step by step, and then run the following procedures until the number of elements in ‘X’ equals a total number of nodes in our graph. At each iteration of a cycle, we create a list of edges we are choosing from on this particular step. Then, for each node, already added to our ‘X’ list, we look at the edges between it and the neighbor node, create a list of all edges between the initial one and neighbors, choose the one with lower weight, and add it to the MST. Then, add a new node (to which we have a path already) to the ‘X’ list, and repeat the iteration.
### Boruvka:
A set ‘MST’ is created to store the resulting tree. A dictionary ‘minEdge’ is created to store the minimal edge for each of current connected components (key - root of a CC, value - minimal edge for it), integer n is made equal to the number of nodes. The array of edges is sorted. A while cycle is runned untill the number of edges in ‘MST’ is equal to n-1 (and therefore it is the wanted tree). On each iteration a cycle runs through the edges to find minimal edges for all current CCs (for any edge we check that its nodes belong to different CCs and if yes, we check if the edge is smaller then edges for those CCs in minEdge, if yes, we put the edge in minEdge. Then a cycle runs through all the nodes, for each of them we check if it is a root of a CC. If yes, we use its minimal edge from minEdge to connect it with another CC (if this edge wasn’t already used) and adds the edge to MST. Before the next iteration minEdge is cleared.

## Drive part: 
### Finding MST (minimal spanning tree): 
First, a graph g is made from given data, then all three algorithms are runned on it, obtained trees are stored as ansK (for Kruskal), ansB (for Boruvka) and ansP (for Prim). All three are compared, and, if all three are equal, which implies that the algorithms are imolemented correctly, line ‘found MST’ is printed out.
### Output (Map Description): 
We imported folium library to create a map. From the Kruskal algorithm, we had a set of all edges in MST. This set consists of tuples, in each tuple there are three objects: start node, finish node, weight. Firstly, we construct markers with coordinates of the cities, using built-in methods of folio library. Secondly, we connect those markers. Coordinates of markers are taken from the properties of the nodes.


**Geocoding.py**
## Drive part:
In geocoding part we used 4 libraries: logging, time, pandas, requests and our Google API key. With God’s help, we have coped with the task. After mentioning all restrictions and extra functions(as Google Full Result). Using Google’s geocode url we got all information about cities in Australia. Also there are some helpful time managing features if we get API Query limit.


**Distance_matrix.py**
## Drive part:
In distance matrix part we used prepared MST and tried to understand if real roads are shorter. So, using pandas, googlemaps and csv we got the final table (Final.csv) where you can see all cities, graph value and km between given cities.
# Result: 
The obtained MST is visualised on a map via Folium library. Also a comparison table is constructed in a form of a .csv file
