import sys
sys.setrecursionlimit(10**6)

def BF(n, tot):
	global sol
	if n == 2 :
		sol = max(tot, sol)
		return
	
	for i in range(1,n-1):
		val = arr[i-1]*arr[i+1]
		tmp = arr[i]
		arr.pop(i)
		BF(n-1, tot+val)
		arr.insert(i,tmp)

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
sol=0

BF(N,0)
print(sol)