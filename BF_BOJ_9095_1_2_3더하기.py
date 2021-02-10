# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.setrecursionlimit(10**6)

def BF(N,tot):
	global cnt
	
	if tot == N:
		cnt+=1
		return
	
	if tot > N : 
		return
	
	for i in [1,2,3]:
		BF(N,tot+i)

	
T = int(input())
arr = []
cnt=0

while T:
	N=int(input())
	cnt=0
	BF(N,0)
	arr.append(cnt)
	T-=1

for n in arr:
	print(n)
