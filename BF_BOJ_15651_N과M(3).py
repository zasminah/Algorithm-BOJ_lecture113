#https://www.acmicpc.net/lecture/113
##https://www.acmicpc.net/problem/15651
#2020년 5월 알고리즘
#N과 M(3)
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.setrecursionlimit(10**6)

def BF(level):
	if level == M :
		print(*arr)
		return
	
	for i in range(1,N+1):
		arr.append(i)
		BF(level+1)
		arr.pop()

N, M = map(int, sys.stdin.readline().split())
arr=[]
visited = [0]*(N+1)

BF(0)	
