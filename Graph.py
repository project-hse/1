class Node:
	# each node initially has itslef as parent and rank 0
	def __init__(self, name, latitude, longitude):
		self.name = name
		self.parent = Node(name, latitude, longitude)
		self.rank = 0
		self.lat = latitude
		self.long = longitude


class Graph:
	# create array of edges, array of nodes
	def __init__(self):
		self.graph = []
		self.nodes = []

	# add edge between "v" & "u" with weight "weight"
	def addEdge(self, v, u, weight):
		self.graph.append([v, u, weight])

	# add node
	def addNode(self, name, latitude, longitude):
		node = Node(name, latitude, longitude)
		self.nodes.append(node)

	# find root of tree vertex belongs to
	def find(self, u):
		if u.parent == u:
			return u
		return self.find(u.parent)


	# connect "u" & "v" in MST
	def connect(self, v, u):
		rootv = self.find(v)
		rootu = self.find(u)

		if rootu.rank > rootv.rank:
			rootv.parent = rootu
		else:
			rootu.parent = rootv
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
			g.addEdge(g.nodes[i], g.nodes[j], weight)
	
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



g = makeGraph("input.txt")
ans = Kruskal(g)

# some output shit

# test output
for i in range(len(ans)):
	print(ans[i][0], ans[i][1], ans[i][2])