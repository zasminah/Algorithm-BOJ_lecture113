#https://www.acmicpc.net/problem/14502
from sys import stdin
from collections import deque
import copy

def QUE():
	arr2=copy.deepcopy(arr)
	#print(arr2)
	que = deque()
	#add all virus in queue
	for y in range(Y):
		for x in range(X):
			if arr2[y][x] == 2 :
				que.append([y,x,0])
	
	while que :
		y,x,t=que.popleft()
		for i in range(4):
			dy= y+direct[i][0]
			dx= x+direct[i][1]
			if dy<0 or dx<0 or dy>=Y or dx>=X: continue
			if arr2[dy][dx] == 0 :
				arr2[dy][dx] = 2 # Virus
				que.append([dy,dx,t+1])
	return count(arr2)
	
def count(arr2):
	cnt = 0
	for y in range(Y):
		for x in range(X):	
			if arr2[y][x] == 0 :
				cnt+=1
	return cnt
				
def BF(n,s):
	global sol
	if n == 3 :
		sol = max(sol,QUE())
		return
	
	for i in range(s,X*Y):
		ny = i//X
		nx = i%X
		if arr[ny][nx] == 0 :
			arr[ny][nx] = 1
			BF(n+1,i)
			arr[ny][nx] = 0				
				
Y,X=  map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(Y)]
arr2 = [[0]*X for _ in range(Y)]
visited = [0]*(X*Y)
direct = [[-1,0],[1,0],[0,-1],[0,1]]
sol=0

BF(0,0)
print(sol)