#https://www.acmicpc.net/problem/16928
from sys import stdin
from collections import deque

def BF():
	que = deque()
	visited[1]=1
	que.append([1,0])
	
	while que:
		l,t=que.popleft() # location, time
		
		if l == 100 : return t
		
		for i in range(1,7):
			nl = l + i # new location = location + dice
			for j,k in arrN:
				if nl == j : nl = k
			for j,k in arrM:
				if nl == j : nl = k
			if nl>=1 and nl<=100 and visited[nl] ==  0 :	
				visited[nl]=1
				que.append([nl,t+1])
			
		
#N : 사다리, #M : 벰	
N, M = map(int, stdin.readline().split())
visited = [0]*101
arrN = [list(map(int,stdin.readline().split())) for _ in range(N)]
arrM = [list(map(int,stdin.readline().split())) for _ in range(M)]

#print(arrN)
#print(arrM)

sol = BF()
print(sol)

