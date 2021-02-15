#https://www.acmicpc.net/problem/1697

import sys
sys.setrecursionlimit(10**6)
from collections import deque

def getParent(n):  #Backtracking - return Parent
	if n == N : return
	parent=visited[n]
	arr.append(parent)
	getParent(parent)
	
def BFS():
	que = deque()
	que.append([N,0])
	while que:
		n,t=que.popleft()
		if n == K :
			arr.append(n)
			getParent(n)
			print(t)
			print(' '.join(map(str,arr[::-1])))
			#print(' '.join(map(str, arr[::-1])))
			return 

		for i in (n+1,n-1,n*2):
			dn=i
			if dn<0 or dn>100000 or visited[dn]!=-1: 
				continue
			visited[dn]=n #Backtracking - save Parent
			que.append([dn,t+1])
	return -1

#0<=N,K<=100000
N, K = map(int, sys.stdin.readline().split())
visited=[-1]*100001
arr=[]

BFS()

