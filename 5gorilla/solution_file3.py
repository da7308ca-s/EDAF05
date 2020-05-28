import math
import time
import sys

sys.setrecursionlimit(10000)

chars = [x for x in input().split()]
alpha = {x: {chars[i]: int(y) for i,y in enumerate(input().split())} for x in chars}#value of pairing two characters
words = [[x for x in input().split()] for i in range(int(input()))] #Read the sequences
delta = -4

debug = "debug" in sys.argv
timers = {"Total time": 0, "First call": 0, "Other calls": 0}
opt_calls = 0
mem_calls = 0

def opt(i,j):
	global opt_calls, mem_calls, memory
	a = memory[i][j]
	if a is not None: #If already computed return it
		mem_calls +=1 
		return a
	if i == 0:
		opt_calls +=1
		memory[i][j] = j*delta, 0
		return memory[i][j]
	if j == 0:
		opt_calls +=1
		memory[i][j] = i*delta, 0
		return memory[i][j]
	opt_calls +=1
	o1, _ = opt(i-1,j-1)
	o2, _ = opt(i,j-1)
	o3, _ = opt(i-1,j)
	vals = [alpha[s[i]][t[j]] + o1 ,delta + o2, delta + o3]
	index = vals.index(max(vals))
	memory[i][j] = (max(vals),index)
	return memory[i][j]

start = time.time()
counter = 0
for s,t in words:
	memory = [[None for i in range(len(t))] for j in range(len(s))] #memory matrix for saving previous calls to opt(i,j)
	i = len(s)-1
	j = len(t)-1
	counter += (i+1)*(j+1)
	sl = [x for x in s] # list of the words were we will insert the "*"
	tl = [x for x in t]
	first = True
	while i>0 or j>0:

		# special case if i == 0 or j == 0
		if i == 0:
			m = -1000
			for k in range(j+1):
				if alpha[s[i]][t[k]] > m:
					m = alpha[s[i]][t[k]]
					index = k
			for k in range(j,-1,-1):
				if not k == index:
					sl.insert(k,"*")
			break
		if j == 0:
			m = -1000
			for k in range(i+1): 
				if alpha[s[k]][t[j]] > m:
					m = alpha[s[k]][t[j]]
					index = k
			for k in range(i,-1,-1):
				if not k == index:
					tl.insert(k,"*")
			break

		# choose the option with the highst score
		start0 = time.time()
		_, index = opt(i,j)
		"""
		vals = [alpha[s[i]][t[j]] + opt(i-1,j-1), dea + opt(i,j-1)lt, delta + opt(i-1,j)]
		index = vals.index(max(vals))
		"""
		if first:				
			timers["First call"] += time.time()-start0
			first = False
		else:
			timers["Other calls"] += time.time()-start0


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
	print("Statistics for " + str(len(words)) + " queries with alphabet size " + str(len(chars)))
	print( '{:,}'.format(opt_calls+mem_calls) + " calls to opt (m*n = " + '{:,}'.format(counter)+")")
	print("of which " +  '{:,}'.format(mem_calls) + " used memory and " + '{:,}'.format(opt_calls) + " were computed" )
	timers["Total time"] = time.time()-start
	timers = sorted(timers.items(), key=lambda item: item[1])
	for k,v in timers[::-1]:
		print('{:20}'.format(k) + " " + "%.6f" %v)
	print("")
