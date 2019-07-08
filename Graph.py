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

	    for index, row in df.iterrows():
        #print(row['input_string'], row['latitude'], row['longitude'])
        g.addNode(row['input_string'], row['latitude'], row['longitude'])

    #fin = open(inputf, 'r')
    #line = fin.readline()
    #while line:  # add nodes to graph g w their coords from file
        #s = line.split()
        #g.addNode(s[0], float(s[1]), float(s[2]))
        #line = fin.readline()
    #fin.close()

	for i in range(len(g.nodes) - 1): #from array of nodes calculate weights, add edges to graph g
		for j in range(i + 1, len(g.nodes)):
			weight = ((g.nodes[i].lat - g.nodes[j].lat)**2 + (g.nodes[i].long - g.nodes[j].long)**2)**0.5
			g.graph.append([g.nodes[i], g.nodes[j], weight])
	
	return g

def Kruskal(g):
	MST = set()
	g.graph = sorted(g.graph, key=lambda item: item[2])

	for i in range(len(g.graph)): #for all edges
		u, v, weight = g.graph[i]
		
		if g.find(u) != g.find(v): #test for cycles
			g.connect(u, v)
			MST.add((u.name, v.name, weight))
		#else not included

	return MST

def Prim(g):
	#Create lists MST and X
	MST = set()
	X = []

	X.append(g.nodes[0]) # Start from the arbitrary node
	while len(X) != len(g.nodes): #For  each node 'x' in a graph
		curr_edges = []                #we add edge from 'x' to 'i' to curr_edges
		for x in X:               #if 'i' is not yet in X
			for i in g.nodes:
				if i not in X:
					weight = ((i.lat - x.lat)**2 + (i.long - x.long)**2)**0.5
					curr_edges.append([i, x, weight])
		#Then find the edge with the smallest weight in a curr_edges, add it to MST
		curr_edges = sorted(curr_edges, key = lambda item: item[2])
		edge = curr_edges[0]

		MST.add((edge[1].name, edge[0].name, edge[2]))
		X.append(edge[0]) #Add new node to X, repeat
	return MST

def Boruvka(g):
	MST = set() #resulting graph
	minEdge = dict() #array of minimal edges for each CC
	n = len(g.nodes) #number of CCs, initially = num of nodes (each node is a CC)

	g.graph = sorted(g.graph, key=lambda item: item[2])

	while len(MST) < n - 1: #while we don't have n-1 edges in MST = while we don't have 1 resulting tree that is MST
		# find minimal edges for all current CCs
		for i in range (len(g.graph)):
			u, v, weight = g.graph[i]
			CC1 = g.find(u) #root of CC of u
			CC2 = g.find(v) #root of CC of v

			if CC1 != CC2: #if v, u not in the same CC
				#if current edge is smaller than edge of CC in minEdge
				if CC1 not in minEdge or minEdge[CC1][2] > weight:
						minEdge[CC1] = [u, v, weight]
				if CC2 not in minEdge or minEdge[CC2][2] > weight:
						minEdge[CC2] = [u, v, weight]
		#now we have minimal edges for all current CC

		#add found edges to MST
		for i in range (len(g.nodes)):
			node = g.nodes[i]

			if node in minEdge: #a node can be not in minEdge if it isn't a root of some CC
				u, v, weight = minEdge[node]
				CC1 = g.find(u) #root of CC of u
				CC2 = g.find(v) #root of CC of v

				if CC1 != CC2: #we could have connected them already if the edge was min for both
					g.connect(CC1, CC2) #unite CCs current edge connects
					MST.add((u.name, v.name, weight))

		#clear dicitonary of minimal edges before next iteration
		minEdge.clear()

	return MST


df = pd.read_csv("Output.csv", usecols = ["input_string", "latitude", "longitude"])
g = makeGraph(df)
ans = Kruskal(g)


ansP = Prim(g)
ansB = Boruvka(g)

for i in g.nodes:
	g.parent[i] = i

ansK = Kruskal(g)

# chek
# ans = ansP.difference(ansK)

# some output shit

# test output
# print("Kruskal")
# for i in ansK:
# 	print(i)
# print("Boruvka")
# for i in ansB:
# 	print(i)
# print("Prim")
# for i in ansP:
# 	print(i)
# print("ans")
# for i in ans:
# 	print(i)
