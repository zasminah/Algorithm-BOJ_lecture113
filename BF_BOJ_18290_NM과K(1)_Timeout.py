# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.setrecursionlimit(10**5)

def checkRange(y,x):
	for i in range(4):
		dy=y+direct[i][0]
		dx=x+direct[i][1]
		if dy<0 or dx<0 or dy>=Y or dx>=X : continue
		if visited[dy][dx] == 1 :
			return 0
	return 1

def BF(tot,level):
	global sol

	if level == K:
		#print(tot)
		#print(visited)
		sol=max(sol, tot)
		return
	
	for _y in range(Y):
		for _x in range(X):
			if visited[_y][_x]==0:
				if checkRange(_y,_x) == 1:
					visited[_y][_x]=1
					BF(tot+arr[_y][_x],level+1)
					visited[_y][_x]=0

Y,X,K=map(int, sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(Y)]
visited = [[0]*X for _ in range(Y)]
direct = [[0,1],[0,-1],[1,0],[-1,0]]

sol=-987654321

BF(0,0)
print(sol)