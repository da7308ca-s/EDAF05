import math
import time
import sys
import copy

class Graph: 
 
	def __init__(self,graph, source, sink):
		self.original_graph = copy.deepcopy(graph)
		self.graph = graph
		self.ROW = len(graph)
		self.paths = []
		self.source = source
		self.sink = sink
   
	def BFS(self,s, t, path):
		visited =[False]*(self.ROW)   
		queue=[self.source] 
		visited[s] = True
		while queue: 
			u = queue.pop(0) 
			for ind, val in enumerate(self.graph[u]):
				if visited[ind] == False and val > 0 : 
					queue.append(ind) 
					visited[ind] = True
					path[ind] = u 
		return True if visited[t] else False
	  
	# Fill in paths with FordFulkerson
	def FillGraph(self): 

		#List for storing path
		path = [-1]*(self.ROW)
		while self.BFS(self.source, self.sink, path) : 

			#Find the flow along the path
			path_flow = float("Inf") 
			s = self.sink 
			while(s !=  self.source): 
				path_flow = min (path_flow, self.graph[path[s]][s]) 
				s = path[s] 
			self.paths.append([copy.deepcopy(path),path_flow])
			# Add path flow to overall flow 
  
			#Take away the capacity of the path
			v = self.sink 
			while(v !=  self.source): 
				u = path[v] 
				self.graph[u][v] -= path_flow 
				self.graph[v][u] -= path_flow 
				v = path[v] 

	def RemoveEdgeAndGetNewFlow(self,edge):
		a, b, edge_flow = edge
		remove_indices = []
		for i, p in enumerate(self.paths):
			path, path_flow = p
			if self.hasEdge(a,b,path):
				remove_indices.append(i)
				v = self.sink 
				while(v !=  self.source): 
					u = path[v] 
					self.graph[u][v] += path_flow 
					self.graph[v][u] += path_flow 
					v = path[v]

		for i in remove_indices[::-1]:
			self.paths.pop(i)

		#Close the capacity of the edge we are taking away
		self.graph[a][b] -= edge_flow 
		self.graph[b][a] -= edge_flow 
		self.FillGraph()
		return self.GetMaxFlow()

	def GetMaxFlow(self):
		max_flow = 0
		for _, path_flow in self.paths:
			max_flow += path_flow
		return max_flow

	def hasEdge(self,u,v,path):
		s = self.sink 
		while(s !=  self.source): 
			if s == u and path[s] == v or s == v and path[s] == u:
				return True 
			s = path[s] 
		return False


def print_matrix(matrix):
	for m in matrix:
		print(m)

debug = "debug" in sys.argv
timers = {"Total time": 0}

#Reead input
N, M, C, P = (int(x) for x in input().split())
edges = [[int(x) for x in input().split()] for i in range(M)]
remove_order = [int(input()) for x in range(P)]

#Build matrix
graph_matrix = [[0 for i in range(N)] for j in range(N)]
for i,j,flow in edges:
	graph_matrix[i][j] = graph_matrix[j][i] = flow

graph = Graph(graph_matrix,0, N-1)
graph.FillGraph()
prev_flow = graph.GetMaxFlow()
for i, j in enumerate(remove_order):
	new_flow = graph.RemoveEdgeAndGetNewFlow(edges[j])
	if new_flow<C:
		print(str(i) + " " + str(prev_flow))
		break
	prev_flow = new_flow
	
