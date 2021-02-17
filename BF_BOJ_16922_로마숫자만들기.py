import sys
sys.setrecursionlimit(10**6)

#XXL XLX LXX are all the same value.
def BF(tot,v,n): 
	if n == N :
		result.add(tot)
		return
	for i in range(v,4):
		BF(tot+arr[i],i,n+1)

N = int(input())
arr = [1,5,10,50]
result = set()

BF(0,0,0)
# print(result)
print(len(result))
