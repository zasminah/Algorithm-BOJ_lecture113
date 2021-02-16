#https://www.acmicpc.net/problem/14226

from collections import deque

def BF():
	que = deque()
	que.append([1,0,0])
	
	while que:
		n,c,t=que.popleft()
		if n == N : return t
		
		#print(n,c,t)
		#copy
		if visited[n][n]==0 :
			visited[n][n]=1
			que.append([n,n,t+1])
		#paste
		if n+c<=N and visited[n+c][c] == 0 and c != 0 : 
			visited[n+c][c]=1
			que.append([n+c,c,t+1])
		#delete
		if n-1 >= 0 and visited[n-1][c] == 0 : 
			visited[n-1][c]=1
			que.append([n-1,c,t+1])
	
N = int(input())
visited = [[0]*(N+1) for _ in range(N+1)]
sol = BF()
print(sol)