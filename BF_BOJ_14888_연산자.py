# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.setrecursionlimit(10**6)

def BF(tot,p,mn,m,d,n):
	#print(tot,p,mn,m,d,n)
	global solMin, solMax
	if n==N :
		solMin=min(solMin,tot)
		solMax=max(solMax,tot)
		return
	
	if n!=0 and p !=0 : BF(tot+arr[n],p-1,mn,m,d,n+1)
	if n!=0 and mn !=0 : BF(tot-arr[n],p,mn-1,m,d,n+1)
	if n!=0 and m !=0 : BF(tot*arr[n],p,mn,m-1,d,n+1)
	if n!=0 and d !=0 : BF(int(tot/arr[n]),p,mn,m,d-1,n+1)


N=int(input())
arr = list(map(int,sys.stdin.readline().split()))
plus,minus,mul,div = map(int,sys.stdin.readline().split()) #+.-,*,/
solMin=10000000000
solMax=-10000000000

BF(arr[0],plus,minus,mul,div,1)
print(solMax)
print(solMin)