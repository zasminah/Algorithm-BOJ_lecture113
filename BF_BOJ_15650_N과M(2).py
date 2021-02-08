#https://www.acmicpc.net/lecture/113
##https://www.acmicpc.net/problem/15650
#2020년 5월 알고리즘
#N과 M(2)
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.setrecursionlimit(10**6)

def BF(n,level):
	if level == M :
		print(*arr)
		return
	
	for i in range(n,N+1):
		if visited[i] == 0 :
			visited[i]=1
			arr.append(i)
			BF(i,level+1)
			visited[i]=0
			arr.pop()

N, M = map(int, sys.stdin.readline().split())
arr=[]
visited = [0]*(N+1)

BF(1,0)	
