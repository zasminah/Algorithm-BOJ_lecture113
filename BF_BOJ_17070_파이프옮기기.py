import sys
# from collections import deque
sys.setrecursionlimit(10**4)

# QUEUE
# def BF():
# 	cnt = 0
# 	que = deque()
# 	que.append([0,1,0])
	
# 	while que :
# 		y,x,d = que.popleft()
# 		# print(y,x,d, arr[y][x])
# 		if y == (N-1) and x == (N-1) :
# 			cnt+=1	

# 		if d == 0 or d == 1 :
# 			if x+1 < N and arr[y][x+1] == 0 : que.append([y,x+1,0])
# 		if d == 2 or d == 1 :
# 			if y+1 < N and arr[y+1][x] == 0 : que.append([y+1,x,2])
# 		if d == 0 or d == 1 or d == 2:
# 			if y+1 < N and x+1 < N :
# 				if arr[y+1][x] == 0 and arr[y][x+1] == 0 and arr[y+1][x+1] == 0 : 
# 					que.append([y+1,x+1,1])
	
# 	return cnt

def BF(y,x,d):
	global cnt
	if y == (N-1) and x == (N-1) :
		cnt+=1
		return
	
	if d == 0 or d == 1 :
		if x+1 < N and arr[y][x+1] == 0 : BF(y,x+1,0)
	if d == 2 or d == 1 :
		if y+1 < N and arr[y+1][x] == 0 : BF(y+1,x,2)
	if d == 0 or d == 1 or d == 2:
		if y+1 < N and x+1 < N :
			if arr[y+1][x] == 0 and arr[y][x+1] == 0 and arr[y+1][x+1] == 0 : 
				BF(y+1,x+1,1)

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
direct = [[0,1],[1,1],[1,0]] # Right, Diagonal, Down
cnt = 0
# cnt = BF()
BF(0,1,0)
print(cnt)
