import sys
from collections import deque

def BFS(y,x,g):
	cnt=1
	que = deque()
	que.append([y,x]) #y,x
	visited[y][x]=g
	while que:
		ny, nx = que.popleft()
		for i in range(4):
			dy = ny+direct[i][0]
			dx = nx+direct[i][1]
			if dy<0 or dx<0 or dy>=Y or dx>=X : continue
			if visited[dy][dx] == -1 and arr[dy][dx] == 0 :
				cnt+=1
				visited[dy][dx] = g
				que.append([dy,dx])	
	return cnt

#Return total # of Group 
def FloodFillG(y,x,g):	
	cnt = 1
	# used = [0]*(group+1)# if list is used, TimeOut Error is occured
	used = set() 
	for i in range(4):
		ny = y+direct[i][0]
		nx = x+direct[i][1]		
		if ny<0 or nx<0 or ny>=Y or nx>=X : continue		
	# 	if used[visited[ny][nx]] == 0 and visited[ny][nx] != -1 : # if list is used, TimeOut Error is occured		
	# 		used[visited[ny][nx]] = 1
	# 		cntg+=arrG[visited[ny][nx]]
	# return cntg%10
		if visited[ny][nx] != -1 : 
			used.add(visited[ny][nx])	
	for g in used:
		cnt+=arrG[g]
		cnt = cnt % 10	
	return cnt
			
Y,X=map(int, sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(Y)]
direct = [[-1,0],[1,0],[0,-1],[0,1]]
visited = [[-1]*X for _ in range(Y)]
#print(arr)
cnt = 0
group = 0 
arrG = [0]

for y in range(Y):
	for x in range(X):
		if visited[y][x] == -1 and arr[y][x] == 0:
			group+=1
			cnt=BFS(y,x,group) # BFS			
			arrG.append(cnt)
# print(visited)
# print(arrG)

for y in range(Y):
	for x in range(X):
		if arr[y][x] == 1:
			arr[y][x] = FloodFillG(y,x,group)
			
for y in range(Y):
	print(''.join(map(str,arr[y])))


