import sys
sys.setrecursionlimit(10**6)


N, C = map(int, sys.stdin.readline().split())
M = int(input())
arr = []
arrC=[0]*(N+1)
result=0

for i in range(M):
	s,e,b=map(int, sys.stdin.readline().split())
	arr.append([s,e,b])

arr.sort(key=lambda x : (x[1],x[0]))

for i in range(M):
	cnt=0
	for j in range(arr[i][0],arr[i][1]):
		cnt=max(cnt, arrC[j])
		
	box=min(arr[i][2], C-cnt)
	result+=box
	for j in range(arr[i][0],arr[i][1]):
		arrC[j]+=box
	
print(result)

	
	



	