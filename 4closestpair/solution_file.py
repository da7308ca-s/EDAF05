import math
import time
import sys

def dist(p1,p2):
	start = time.time()
	d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
	if debug:
		timers["dist"]+= time.time()-start
	return d

def bruteForce(points):
	start = time.time()
	min_dist = math.inf
	for p1 in points:
		for p2 in points:
			if not p1 is p2:
				min_dist = min(dist(p1,p2),min_dist)
	if debug:
		timers["bruteForce"]+= time.time()-start
	return min_dist

def closestInStrip(strip,d):
	start = time.time()
	for i in range(len(strip)):
		j = i+1
		while j<len(strip) and (strip[j][1] - strip[i][1]) < d:
			d = min(dist(strip[j],strip[i]),d)
			j+=1
	if debug:
		timers["closestInStrip"]+= time.time()-start
	return d

def sortPoints(points):
	start = time.time()
	px = sorted(points,key = lambda s: s[0])
	py = sorted(points,key = lambda s: s[1])
	if debug:
		timers["sortPoints"]= time.time()-start
	return px, py

def f(px, py, n):
	if n<4:
		return(bruteForce(px))

	mid = n//2
	midPoint = px[mid]
	pxl = px[:mid]
	pxr = px[mid:]
	pyl = []
	pyr = []
	start = time.time()
	for p in py:
		if p[0] <= midPoint[0]:
			pyl.append(p)
		else:
			pyr.append(p)
	if debug:
		timers["divideYpoints"] += time.time()-start

	d = min(f(pxl,pyl,mid),f(pxr,pyr,n-mid))

	start = time.time()
	strip = []
	for p in py:
		if abs(midPoint[0]-p[0])<d:
			strip.append(p)
	if debug:
		timers["createStrips"]+= time.time()-start

	return closestInStrip(strip,d)

debug = "debug" in sys.argv
timers = {"total": 0, "closestInStrip": 0, "bruteForce": 0, "dist": 0, "sortPoints": 0,"divideYpoints": 0,"createStrips": 0}

#Read input
N = int(input())
points = [[int(x) for x in input().split()] for i in range(N)]

#Sort points by x and y coordinates in two lists
px, py = sortPoints(points)

start = time.time()
res = "%.6f" %round(f(px,py,N),6)
if debug:
	print("Statistics for input of " + str(N) + " points")
	timers["total"]= time.time()-start
	timers = sorted(timers.items(), key=lambda item: item[1])
	for k,v in timers[::-1]:
		print('{:20}'.format(k) + " " + "%.6f" %v)
	print("")

print(res)

