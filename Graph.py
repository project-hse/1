class Node:
	# each node initially has itslef as parent and rank 0
	def __init__(self, name, latitude, longitude):
		self.name = name
		self.rank = 0
		self.lat = latitude
		self.long = longitude

	def __str__(self):
		s = self.name + ' ' + str(self.long) + ' ' + str(self.lat)
		return s


class Graph:
	# create array of edges, array of nodes
	def __init__(self):
		self.graph = []
		self.nodes = []
		self.parent = dict()

	# add node
	def addNode(self, name, latitude, longitude):
		node = Node(name, latitude, longitude)
		self.nodes.append(node)
		self.parent[node] = node

	# find root of tree vertex belongs to
	def find(self, u):
		if self.parent[u] == u:
			return u
		return self.find(self.parent[u])


	# connect "u" & "v" in MST
	def connect(self, v, u):
		rootv = self.find(v)
		rootu = self.find(u)

		if rootu.rank > rootv.rank:
			self.parent[rootv] = rootu
		else:
			self.parent[rootu] = rootv
			if rootu.rank == rootv.rank:
				rootv.rank += 1


# make a file of cities w coords into graph
def makeGraph(inputf):
	g = Graph()

	fin = open(inputf, 'r')
	line = fin.readline()
	while line: #add nodes to graph g w their coords from file
		s = line.split()
		g.addNode(s[0], float(s[1]), float(s[2]))
		line = fin.readline()
	fin.close()

	for i in range(len(g.nodes) - 1): #from array of nodes calculate weights, add edges to graph g
		for j in range(i + 1, len(g.nodes)):
			weight = ((g.nodes[i].lat - g.nodes[j].lat)**2 + (g.nodes[i].long - g.nodes[j].long)**2)**0.5
			g.graph.append([g.nodes[i], g.nodes[j], weight])
	
	return g

def Kruskal(g):
	MST = []
	g.graph = sorted(g.graph, key=lambda item: item[2])

	for i in range(len(g.graph)): #for all edges
		u, v, weight = g.graph[i]
		
		if g.find(u) != g.find(v): #test for cycles
			g.connect(u, v)
			MST.append([u, v, weight])
		#else not included

	return MST

def Prim(g):
    #Create lists MST and X
    MST = []
    X = []

    X.append(g.nodes[0]) # Start from the arbitrary node
    while len(X) != len(g.nodes): #For  each node 'x' in a graph
        curr_edges = []                #we add edge from 'x' to 'i' to curr_edges
        for x in X:               #if 'i' is not yet in X
            for i in g.nodes:
                weight = ((i.lat - x.lat)**2 + (i.long - x.long)**2)**0.5
                if i not in X and weight != 0:
                    curr_edges.append([i, x, weight])
        #Then find the edge with the smallest weight in a curr_edges, add it to MST
        curr_edges = sorted(curr_edges, key = lambda item: item[2])
        edge = curr_edges[0]
        print (edge)

        MST.append([edge])
        X.append(edge[0]) #Add new node to X, repeat
    return MST



g = makeGraph("input.txt")
ans = Kruskal(g)

# some output shit

# test output
# for i in range(len(ans)):
# 	print(ans[i][0], ans[i][1], ans[i][2])
