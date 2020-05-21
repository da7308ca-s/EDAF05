import math
import time
import sys

chars2index = {x:i for i,x in enumerate(input().split())}
alpha = [[int(x) for x in input().split()] for k in range(len(chars2index))]
Q = int(input())
words = [[x for x in input().split()] for i in range(Q)]
delta = -4

def opt(i,j):
	if i == 0:
		return j*delta
	if j == 0:
		return i*delta
	global memory
	if memory[i][j] is not None:
		return memory[i][j]
	memory[i][j] = max([alpha[chars2index[s[i]]][chars2index[t[j]]] + opt(i-1,j-1) ,delta + opt(i,j-1), delta + opt(i-1,j)])
	return memory[i][j]

for s,t in words:
	memory = [[None for i in range(len(t))] for j in range(len(s))]
	i = len(s)-1
	j = len(t)-1
	sl = [x for x in s]
	tl = [x for x in t]
	while i>0 or j>0:
		vals = [alpha[chars2index[s[i]]][chars2index[t[j]]] + opt(i-1,j-1) ,delta + opt(i,j-1), delta + opt(i-1,j)]
		if i == 0:
			vals.append(j*delta)
		if j == 0:
			vals.append(i*delta)
		index = vals.index(max(vals))
		if index == 3:
			if i == 0:
				sl.insert(0,"*"*j)
				break
			if j == 0:
				tl.insert(0,"*"*i)
				break
		if index == 0:
			i-=1
			j-=1
		elif index == 1:	
			sl.insert(i+1,"*")
			j-=1
		elif index == 2:
			tl.insert(j+1,"*")
			i-=1
	print("".join(sl) + " " + "".join(tl))

