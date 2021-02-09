# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.setrecursionlimit(10**8)

def checkRange(i,level):
	for j in range(level):
		ref=used[j]
		if i%X != 0 and ref+1 == i : return 0
		if ref+X == i : return 0
	return 1

def BF(s,tot,level):
	global sol

	if level == K:
		#print(used)
		sol=max(sol, tot)
		return
	
	for i in range(s,val):
		if visited[i] == 0:
			if checkRange(i,level) == 1:
				visited[i] = 1
				used[level]=i
				BF(i,tot+arr_[i],level+1)
				visited[i] = 0

Y,X,K=map(int, sys.stdin.readline().split())
val=Y*X
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(Y)]
arr_=[]
visited = [0]*val
used = [0]*K

sol=-987654321

for y in range(Y):
	for x in range(X):
		 arr_.append(arr[y][x])
#print(arr_)
BF(0,0,0)
print(sol)