import pandas as pd
import csv
import folium
class Node:
	# each node initially has itslef as parent and rank 0
	def __init__(self, name, latitude, longitude):
		self.name = name
		self.rank = 0
		self.lat = latitude
		self.long = longitude


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
		g.addNode(row['input_string'], row['latitude'], row['longitude'])

	for i in range(len(g.nodes) - 1): #from array of nodes calculate weights, add edges to graph g
		for j in range(i + 1, len(g.nodes)):
			weight = 100 * ((g.nodes[i].lat - g.nodes[j].lat)**2 + (g.nodes[i].long - g.nodes[j].long)**2)**0.5
			g.graph.append([g.nodes[i], g.nodes[j], weight])
	
	return g

def Kruskal(g):
	MST = set()
	g.graph = sorted(g.graph, key=lambda item: item[2])

	for i in g.graph: #for all edges
		u, v, weight = i
		
		if g.find(u) != g.find(v): #test for cycles
			g.connect(u, v)
			MST.add((u, v, weight))
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
					weight = 100 * ((i.lat - x.lat)**2 + (i.long - x.long)**2)**0.5
					curr_edges.append([i, x, weight])
		#Then find the edge with the smallest weight in a curr_edges, add it to MST
		curr_edges = sorted(curr_edges, key = lambda item: item[2])
		edge = curr_edges[0]

		MST.add((edge[0], edge[1], edge[2]))
		X.append(edge[0]) #Add new node to X, repeat
	return MST

def Boruvka(g):
	MST = set() #resulting graph
	minEdge = dict() #array of minimal edges for each CC
	n = len(g.nodes) #number of CCs, initially = num of nodes (each node is a CC)

	g.graph = sorted(g.graph, key=lambda item: item[2])

	while len(MST) < n - 1: #while we don't have n-1 edges in MST = while we don't have 1 resulting tree that is MST
		# find minimal edges for all current CCs
		for i in g.graph:
			u, v, weight = i
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
		for node in g.nodes:
			if node in minEdge: #a node can be not in minEdge if it isn't a root of some CC
				u, v, weight = minEdge[node]
				CC1 = g.find(u) #root of CC of u
				CC2 = g.find(v) #root of CC of v

				if CC1 != CC2: #we could have connected them already if the edge was min for both
					g.connect(CC1, CC2) #unite CCs current edge connects
					MST.add((u, v, weight))

		#clear dicitonary of minimal edges before next iteration
		minEdge.clear()

	return MST

def equal(set1, set2):
	ans = True
	for i in set1:
		rev = (i[1], i[0], i[2])
		if not (i in set2 or rev in set2):
			ans = False
			break
	for i in set2:
		rev = (i[1], i[0], i[2])
		if not (i in set1 or rev in set1):
			ans = False
			break
	return ans


df = pd.read_csv("Output.csv", usecols = ["input_string", "latitude", "longitude"])
g = makeGraph(df)

ansP = Prim(g)
ansB = Boruvka(g)

for i in g.nodes:
	g.parent[i] = i

ansK = Kruskal(g)
data = set()
for i in ansK:
    data.add((i[0].name, i[1].name, i[2]))
with open('Output1.csv', 'w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['City 1', 'City 2', 'Graph'])
    for row in data:
        csv_out.writerow(row)

# check
if equal(ansP, ansK) and (ansK >= ansB and ansK <= ansB) and equal(ansB, ansP):
	print('found MST')

coord = [-35, 149]
coord.reverse

my_map = folium.Map(location = coord)

for i in ansK:
  folium.Marker([i[0].lat, i[0].long], popup=i[0].name, tooltip='Click').add_to(my_map)
  folium.Marker([i[1].lat, i[1].long], popup=i[1].name, tooltip='Click').add_to(my_map)

for k in ansK:
  points = [[k[0].lat, k[0].long], [k[1].lat, k[1].long]]
  folium.PolyLine(points, color="purple", weight = 1, opacity = 1).add_to(my_map)
