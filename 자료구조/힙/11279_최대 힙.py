import sys
import heapq

read=sys.stdin.readline

N=int(read())
heap=[]

for _ in range(N):
	a=int(read())
	if a==0:
		if heap:
			print(heapq.heappop(heap) [1])
		else:
			print("0")
	else:
		heapq.heappush(heap,(-a,a))  #최대힙 + 원소추가
