# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.setrecursionlimit(10**6)

def BF(s,tot):
	global sol
	if s>=N :
		#print(sol)
		if s==N:	tot_=sum(tot)
		else : tot_=sum(tot[:-1])
		sol=max(sol,tot_)
		return
	
	#상담 안하는 경우
	BF(s+1,tot)	
	#상담하는 경우
	BF(s+arr[s][0],tot+[arr[s][1]])
	
N=int(input())
arr=[list(map(int, input().split())) for _ in range(N)]
sol=0
	
BF(0,[])
print(sol)