#https://www.acmicpc.net/lecture/113
#https://www.acmicpc.net/problem/2529
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.setrecursionlimit(10**6)

def BF(n,level,num):
	#global minV, maxV
	global minC, maxC
	if level>N:

#그리고 0부터 시작하므로 가장 첫번째로 완성된 문자열은 최솟값이고 가장 마지막에 만든 문자열이 최댓값이다.
		# if minV > int(num):
		# 	minV=int(num)
		# 	minC=num
		# if maxV < int(num):
		# 	maxV=int(num)
		# 	maxC=num
		
		if not len(minC): minC=num
		else : maxC=num
		return
	
	for i in range(10):
		if used[i]==0 :
			if level>0 :
				if (sign[level-1] == '<' and i>n) or (sign[level-1] == '>' and n>i):
					used[i]=1
					BF(i,level+1,num+str(i))
					used[i]=0
			else:
				used[i]=1
				BF(i,level+1, num+str(i))
				used[i]=0
				
N=int(input())
sign = list(sys.stdin.readline().split())
used = [0]*10
# maxV=0
# minV=9999999999
maxC,minC='',''

BF(0,0,'')
print(maxC)
print(minC)
