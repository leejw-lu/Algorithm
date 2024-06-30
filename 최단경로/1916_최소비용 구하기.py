#다익스트라
import sys
import heapq
input=sys.stdin.readline

INF=int(1e9)

n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b,w= map(int,input().split())
    graph[a].append((b,w))

start, end= map(int,input().split())

distance=[INF]*(n+1)

def dijkstra(idx):
    distance[idx]=0
    q=[(0, start)]

    while q:
        w, cur= heapq.heappop(q) #가장 최단cost 노드 구하기(최소heap)
        if distance[cur]<w: #이미 갱신 된
            continue
        
        for dest, wei in graph[cur]:
            cost=distance[cur]+ wei
            if distance[dest]>cost:
                distance[dest]=cost #갱신
                heapq.heappush(q,(cost, dest))

dijkstra(start)
print(distance[end])
