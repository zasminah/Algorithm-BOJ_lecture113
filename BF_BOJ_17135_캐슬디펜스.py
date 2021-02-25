# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
import copy
sys.setrecursionlimit(10**6)

def calcDist(y1,x1,y2,x2):
	return abs(y1-y2)+abs(x1-x2)

def attack(select,n):
	global cnt,arr2
	if n < 0 : 
		return
	
	e = n-K-1
	if e < 0 : e = -1 
	
	location = []
	
	for j in select:
		minx = X
		miny = n
		mind = 11 # max Val + 1
		flag = 0
		
		for y in range(n-1,e,-1):
			for x in range(X):# (y,x)
				# print(j, n-1,e, y,x, arr2[y][x])
				if arr2[y][x] == 0 : continue
				dist = calcDist(y,x,n,j)
				# print("dist: ",y,x,dist, mind)
				if dist <= K :
					if dist < mind or (dist == mind and minx > x) :
						flag = 1 # need to update 
						mind = dist
						minx = x
						miny = y 
		if flag == 1 : 
			# print("min: ",miny,minx)
			location.append([miny,minx])			
	
	location = set(list(map(tuple,location)))
	# print(location)
	# Map update 
	for y,x in location :
		cnt+=1
		arr2[y][x]=0
	
	attack(select, n-1)
	

def BF(n,level):
	global cnt, maxcnt, arr2
	if level == 3 :
		# print(select)
		arr2 = copy.deepcopy(arr)
		cnt=0
		attack(select,Y)
		maxcnt = max(cnt, maxcnt)
		# print(maxcnt)
		return
	
	for i in range(n,X):
		if visited[i] == 0 :
			select.append(i)
			visited[i]=1
			BF(i,level+1)
			select.pop()
			visited[i]=0
		
Y,X,K = map(int,sys.stdin.readline().split())
select=[]
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(Y)]
arr2 = copy.deepcopy(arr)
visited=[0]*X
cnt, maxcnt = 0,0

# attack([1,2,3],Y)
BF(0,0)
print(maxcnt)
