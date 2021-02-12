# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.setrecursionlimit(10**6)

def calc(tbl) :
	tot=0
	for i in tbl :
		for j in tbl :
			if i==j : continue
			#print(i,j)
			tot+=arr[i-1][j-1]
	return tot
	

def BF(s,n):
	global start
	global link
	global minV
	if n==N/2:
		for i in range(1,N+1):
			if used[i] == 1 : start.append(i)
			else : link.append(i)
		valS=calc(start)
		#print('S',start,valS)
		valL=calc(link)
		#print('L',link,valL)
		start=[]
		link=[]
		minV=min(minV,abs(valS-valL))
		
	for i in range(s,N+1):
		if used[i]==0:
			used[i]=1
			BF(i,n+1)
			used[i]=0

N=int(input())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
used = [0]*(N+1) 
start = []
link = []
minV = 987654321 ;

#print(arr)

BF(1,0)
print(minV)

