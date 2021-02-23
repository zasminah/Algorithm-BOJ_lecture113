# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.setrecursionlimit(10**6)

def BF(y,x,val,level):
	global result
	if level == 6 : 
		result.add(val)
		return		
		
	for i in range(4):
		dy = y + direct[i][0]
		dx = x + direct[i][1]
		if dy<0 or dx<0 or dy>=5 or dx>=5 : continue
		BF(dy,dx,val+str(arr[dy][dx]),level+1)
		

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(5)]
result = set()
direct = [[-1,0,],[1,0],[0,1],[0,-1]]

for y in range(5):
	for x in range(5):
		BF(y,x,'',0)

print(len(result))