import math
import time
import sys

sys.setrecursionlimit(10000)

chars2index = {x:i for i,x in enumerate(input().split())} #Convert character to index in alpha matrix
alpha = [[int(x) for x in input().split()] for k in range(len(chars2index))] #value of pairing two characters
Q = int(input())
words = [[x for x in input().split()] for i in range(Q)] #Read the sequences
delta = -4

debug = "debug" in sys.argv
timers = {"Total time": 0, "opt_compute": 0, "opt_memory": 0}
opt_calls = 0
mem_calls = 0

def opt(i,j):
	start = time.time()
	global opt_calls, mem_calls
	opt_calls +=1
	if i == 0:
		return j*delta
	if j == 0:
		return i*delta
	global memory
	if memory[i][j] is not None: #If already computed return it
		mem_calls +=1 
		timers["opt_memory"] += time.time()-start
		return memory[i][j]
	memory[i][j] = max([alpha[chars2index[s[i]]][chars2index[t[j]]] + opt(i-1,j-1) ,delta + opt(i,j-1), delta + opt(i-1,j)])
	return memory[i][j]

start = time.time()
for s,t in words:
	memory = [[None for i in range(len(t))] for j in range(len(s))] #memory matrix for saving previous calls to opt(i,j)
	i = len(s)-1
	j = len(t)-1
	sl = [x for x in s] # list of the words were we will insert the "*"
	tl = [x for x in t]
	while i>0 or j>0:

		# special case if i == 0 or j == 0
		if i == 0:
			m = -1000
			for k in range(j+1):
				if alpha[chars2index[s[i]]][chars2index[t[k]]] >= m:
					m = alpha[chars2index[s[i]]][chars2index[t[k]]]
					index = k
			for k in range(j,-1,-1):
				if not k == index:
					sl.insert(k,"*")
			break
		if j == 0:
			m = -1000
			for k in range(i+1):
				if alpha[chars2index[s[k]]][chars2index[t[j]]] >= m:
					m = alpha[chars2index[s[k]]][chars2index[t[j]]]
					index = k
			for k in range(i,-1,-1):
				if not k == index:
					tl.insert(k,"*")
			break

		# choose the option with the highst score
		start0 = time.time()
		vals = [alpha[chars2index[s[i]]][chars2index[t[j]]] + opt(i-1,j-1), delta + opt(i,j-1), delta + opt(i-1,j)]
		timers["opt_compute"] += time.time()-start0
		index = vals.index(max(vals))
		if index == 0:
			i-=1
			j-=1
		elif index == 1:	
			sl.insert(i+1,"*")
			j-=1
		elif index == 2:
			tl.insert(j+1,"*")
			i-=1
	if not debug:
		print("".join(sl) + " " + "".join(tl))

if debug:
	print("Statistics for " + str(Q) + " queries with alphabet size " + str(len(chars2index)))
	print(str(opt_calls) + " calls to opt of which " +  str(mem_calls) + " used memory (" +str((mem_calls/opt_calls)*100) + "%)" )
	timers["Total time"] = time.time()-start
	timers = sorted(timers.items(), key=lambda item: item[1])
	for k,v in timers[::-1]:
		print('{:20}'.format(k) + " " + "%.6f" %v)
	print("")

