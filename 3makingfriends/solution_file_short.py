N, M = (int(x) for x in input().split()) #N = number of nodes, M = number of possible edges
nodes = [[[i],0] for i in range(N)] #One slot for every node, where the element at index i is a tuple with the tree that node i belongs to and the tree weight
for u, v, w in sorted([[int(x)-1 for x in input().split()] for i in range(M)], key = lambda s: s[2]):#iterate edges sorted by weight; u = node_index_1, v = node_index_2, w = weight
	if not nodes[u] is nodes[v]: #If the trees are not the same, connect them
		t1, t2 = (nodes[v], nodes[u]) if len(nodes[u][0]) < (len(nodes[v][0])) else (nodes[u],nodes[v])#Reverse the variables so the smaller tree connects to the bigger tree
		t1[1] += t2[1] + w + 1 #Sum the weights
		t1[0] += t2[0] #Unite with nodes from t2
		for i in t2[0]:#Make sure the nodes in t2 now point at t1
			nodes[i] = t1
		if len(t1[0]) == N:#If a tree connects all nodes, finish and print the weight of that tree
			print(t1[1])
			break