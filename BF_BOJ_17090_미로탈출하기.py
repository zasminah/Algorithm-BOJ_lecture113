import sys
sys.setrecursionlimit(10**6)

def BF(y,x):
	global res
	if y<0 or x<0 or y>=Y or x>=X :
		res = 1
		return 1
	if visited[y][x] != -1 :
		return visited[y][x]
	
	dy,dx=y,x
	visited[y][x] = 0 # initial value
	
	if arr[y][x] == 'U' : dy-=1
	if arr[y][x] == 'D' : dy+=1
	if arr[y][x] == 'R' : dx+=1
	if arr[y][x] == 'L' : dx-=1
	
	val = BF(dy,dx)
	visited[y][x] = val 
	return val

Y,X = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(Y)]
cnt = 0
res = 0 
visited = [[-1]*X for _ in range(Y)]

for y in range(Y):
	for x in range(X):
		val=BF(y,x)
		cnt+=val

# print(arr)
print(cnt)