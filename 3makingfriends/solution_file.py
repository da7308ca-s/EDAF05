class Tree:
	def __init__(self,node_indices, weight = 0):
		self.nodes = node_indices #The indices of the nodes that make up this tree
		self.weight = weight #The summed up weights of all the edges that make up this tree

	#Connect a tree to this tree
	def adopt(self,tree, w):
		self.nodes += tree.nodes
		self.weight += tree.weight +w

N, M = (int(x) for x in input().split()) #N = number of nodes, M = number of possible edges
nodes = [Tree([i]) for i in range(N)] #One slot for every node, where the element at index i is the tree that node i belongs to
edges = [] #All the edges stored in a (node_index_1, node_index_2, weight) format

#Read all the edges
for i in range(M):
	nums = input().split()
	u = int(nums[0])-1
	v = int(nums[1])-1
	w = int(nums[2])
	edges.append((u,v,w))

#Sort the edges by their weight and iterate through them
for u, v, w in sorted(edges,key = lambda s: s[2]): #u = node_index_1, v = node_index_2, w = weight
	t1, t2 = nodes[u], nodes[v] #The first and second tree

	 #If the trees are not the same, connect them
	if not t1 is t2:

		#Reverse the variables so the bigger tree adopts the smaller tree
		if len(t1.nodes) < (len(t2.nodes)):
			t1, t2 = t2, t1

		t1.adopt(t2,w)

		#Make sure the nodes in t2 now point at t1
		for i in t2.nodes:
			nodes[i] = t1

		#If a tree connects all nodes, finish and print the weight of that tree
		if len(t1.nodes) == N:
			print(t1.weight)
			break