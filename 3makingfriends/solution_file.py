from operator import itemgetter

class Tree:

	def __init__(self,node_indices, weight = 0):
		self.nodes = node_indices
		self.weight = weight

	def connect(self,tree, w):
		return Tree(self.nodes+tree.nodes, self.weight + tree.weight + w)

	def adopt(self,tree, w):
		self.nodes += tree.nodes
		self.weight += tree.weight +w

	def print_tree(self):
		text = "Nodes:"
		for i in self.nodes:
			text+= " " + str(i)
		print(text)
		print("Weight", self.weight)

#Read input parameters
nums = input().split()
N = int(nums[0])
M = int(nums[1])

nodes = [Tree([i]) for i in range(N)]
edges = []

for i in range(M):
	nums = input().split()
	u = int(nums[0])-1
	v = int(nums[1])-1
	w = int(nums[2])
	edges.append((u,v,w))

edges = sorted(edges,key=itemgetter(2))

for u, v, w in edges:
	t1 = nodes[u]
	t2 = nodes[v]
	if not t1 == t2:
		if len(t1.nodes) < (len(t2.nodes)):
			t2.adopt(t1,w)
			for i in t1.nodes:
				nodes[i] = t2
			if len(t2.nodes) == N:
				print(t2.weight)
				break
		else:
			t1.adopt(t2,w)
			for i in t2.nodes:
				nodes[i] = t1
			if len(t1.nodes) == N:
				print(t1.weight)
				break





