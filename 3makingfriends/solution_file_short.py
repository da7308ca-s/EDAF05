N, M = (int(x) for x in input().split()) #N = number of nodes, M = number of possible edges
nodes = [[[i],0] for i in range(N)] #One slot for every node, where the element at index i is a tuple with the tree that node i belongs to and the tree weight
for u, v, w in sorted([[int(x)-1 for x in input().split()] for i in range(M)], key = lambda s: s[2]):#iterate edges sorted by weight; u = node_index_1, v = node_index_2, w = weight
	t1, t2 = nodes[u], nodes[v]#The first and second tree
	if not t1 is t2: #If the trees are not the same, connect them
		if len(t1[0]) < (len(t2[0])):#Reverse the variables so the bigger tree connects the smaller tree
			t1, t2 = t2, t1
		t1[1] += t2[1] + w + 1 #Sum the weights
		t1[0] += t2[0] #Unite with nodes from t2
		for i in t2[0]:#Make sure the nodes in t2 now point at t1
			nodes[i] = t1
		if len(t1[0]) == N:#If a tree connects all nodes, finish and print the weight of that tree
			print(t1[1])
			break