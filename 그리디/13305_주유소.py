import sys
read=sys.stdin.readline

N=int(read())
distance=list(map(int,read().split()))
cost=list(map(int,read().split()))

minCost=cost[0]
result=0

for i in range(N-1):
    if minCost>cost[i]:
        minCost=cost[i]
    result+=(minCost*distance[i])

print(result)
