import sys
import heapq

read=sys.stdin.readline

N=int(read())
heap=[]

for _ in range(N):
	a=int(read())
	if a==0:
		if heap:
			print(heapq.heappop(heap))
		else:
			print("0")
	else:
		heapq.heappush(heap,a)