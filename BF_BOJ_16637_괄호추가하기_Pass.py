import sys
import copy
sys.setrecursionlimit(10**6)

def cal(a,opr,b):
	if opr == '+' : return a+b
	elif opr == '-' : return a-b
	elif opr == '*' : return a*b
	
def BF(n,flag):
	global maxV
	if n >= N :
		# print(select)
		val=int(select[0])
		for i in range(0,len(select)-2,2):
			val = cal(val,select[i+1],int(select[i+2]))
		# print(val)	
		maxV=max(val,maxV)
		return 
	
	#Not Select
	select.append(arr[n])
	BF(n+1,0)
	select.pop()	
		
	#Select
	if n <= N-3 and n%2 == 0 and flag == 0 :
		val = cal(int(arr[n]),arr[n+1],int(arr[n+2]))
		select.append(str(val))
		BF(n+3,1)
		select.pop()

N = int(input())
arr = list(sys.stdin.readline().strip())
arr2 = copy.deepcopy(arr)
select = []
maxV = -2**31

BF(0,0)
print(maxV)