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
   
	def BFS(self,s, t, parent):
		visited =[False]*(self.ROW)   
		queue=[self.source] 
		visited[s] = True
		while queue: 
			u = queue.pop(0) 
			for ind, val in enumerate(self.graph[u]):
				if visited[ind] == False and val > 0 : 
					queue.append(ind) 
					visited[ind] = True
					parent[ind] = u 
		return True if visited[t] else False
	  
	# Fill in paths with FordFulkerson
	def FordFulkerson(self): 

		#List for storing path
		parent = [-1]*(self.ROW)
		while self.BFS(self.source, self.sink, parent) : 

			#Find the flow along the path
			path_flow = float("Inf") 
			s = self.sink 
			while(s !=  self.source): 
				path_flow = min (path_flow, self.graph[parent[s]][s]) 
				s = parent[s] 
			self.paths.append([copy.deepcopy(parent),path_flow])
			# Add path flow to overall flow 
  
			#Take away the capacity of the path
			v = self.sink 
			while(v !=  self.source): 
				u = parent[v] 
				self.graph[u][v] -= path_flow 
				self.graph[v][u] -= path_flow 
				v = parent[v] 
			print("graph")
			print_matrix(self.graph)

	def GetMaxFlow(self):
		max_flow = 0
		for _, path_flow in self.paths:
			max_flow += path_flow
		return max_flow

def remove_edge(graph_matrix,edge):
	i,j, _ = edge
	graph_matrix[i][j] = graph_matrix[j][i] = 0
	return graph_matrix

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
graph.FordFulkerson()
