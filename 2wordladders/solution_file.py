import sys
import time

class Node:
	def __init__(self,word):
		self.word = word
		self.discovered = False
		self.level = 0

	#Finds the arcs for each node and saves them in a list
	def find_arcs(self,nodes):
		self.arcs = []

		#Loop over all the other nodes
		for w, n in nodes.items():
			if w == self.word:
				continue

			is_connected = True
			used_indices = []

			#Loop over the last for letters in the word
			for letter in self.word[1:]:
				found_letter = False

				#Loop over the letters in the other word we are comparing with
				for i, l in enumerate(w):

					#If a match is found mark that letter as found and save 
					#the index letter of the word we are comparing with so it cant be matched again
					if letter == l and i not in used_indices:
						used_indices.append(i)
						found_letter = True
						break

				#If a letter cannot be matched we know there is no arc and we don't have to evaluate the other letters
				if not found_letter:
					is_connected = False
					break

			if is_connected:
				self.arcs.append(n)

	#Helper method for cheking each node has the right arcs
	def print_arcs(self):
		text = self.word + ": "
		for n in self.arcs:
			text+= n.word + " "
		print(text)

#BFS for finding length of pass from start, O(|V| + |E|) since every node and every edge will be explored once in worstcase
def find_path(start_node,goal):

	#Create a queue (list in python) and mark the first node as discovered 
	start_node.discovered = True
	queue = [start_node]
	while len(queue)>0:

		#Evaluate the node first in the queue
		node = queue.pop(0)

		#If we reach the goal node return the level of that node
		if node.word == goal:
			return node.level

		#Loop over the connected nodes and append them to the queue if they have not been discovered 
		for child in node.arcs:
			if not child.discovered:
				child.discovered = True
				child.level = node.level + 1 #Increase the level to one more than it's parent
				queue.append(child)
	return "Impossible"

debug = "debug" in sys.argv

#Read input parameters
N, Q = (int(x) for x in input().split())

if debug:
	start = time.time()
#Store the nodes in a dict for faster lookup
nodes = {}
for i in range(N):
	word = input()
	nodes[word] = Node(word)

if debug:
	print('{:20}'.format("Initiate nodes"), time.time()-start)

if debug:
	start = time.time()
queries = []
for i in range(Q):
	queries.append(input().split())
if debug:
	print('{:20}'.format("Read queries"), time.time()-start)

if debug:
	start = time.time()

#Find the arcs for each node
for n in nodes.values():
	n.find_arcs(nodes)

if debug:
	print('{:20}'.format("Find arcs for each node"), time.time()-start)

if debug:
	t = time.time()

#Find the path for each query
for start, goal in queries:
	if not debug:	
		print(find_path(nodes[start],goal))

	#Dont forget to reset the discovered label and level attribute between each query
	for n in nodes.values():
		n.discovered = False
		n.level = 0

if debug:
	print('{:20}'.format("BFS"), time.time()-t)