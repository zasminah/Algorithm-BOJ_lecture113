import sys
import copy
sys.setrecursionlimit(10**6)

def calc(val,opr,n):
	if opr == '+' : val+=int(arr2[n])
	elif opr == '-' : val-=int(arr2[n])
	elif opr == '*' : val*=int(arr2[n])
	if n+1 >= len(arr2):
		return val	
	return calc(val,arr2[n+1],n+2)

def refactoring():
	for i in select[::-1]:		
		val = 0
		if arr[i+1] == '+' : val = int(arr[i]) + int(arr[i+2])
		elif arr[i+1] == '-' : val = int(arr[i]) - int(arr[i+2])
		elif arr[i+1] == '*' : val = int(arr[i]) * int(arr[i+2])
		for j in range(3) : 
			del arr2[i]
		arr2.insert(i,str(val))		
	return calc(int(arr2[0]),arr2[1],2)
	
def BF(n,flag):
	global arr2
	global maxV
	if n >= N-2 :
		arr2 = copy.deepcopy(arr)
		sol = refactoring()
		if sol != None : maxV=max(maxV, sol)
		return maxV	
	#Not Select
	if n%2 == 0 : BF(n+1,0)
	else : BF(n+1,flag)	
	#Select
	if n%2 == 0 and flag == 0 :
		select.append(n)
		BF(n+1,1)
		select.pop()

N = int(input())
arr = list(sys.stdin.readline().strip())
arr2 = copy.deepcopy(arr)
select = []
maxV = -2**31

BF(0,0)
print(maxV)