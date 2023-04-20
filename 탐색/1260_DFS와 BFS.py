import sys
from collections import deque

read=sys.stdin.readline

def dfs(idx):
    global visited
    visited[idx]=True
    print(idx, end=' ')
    for next in range(1,N+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs():
    global q, visited2
    while q:
        cur=q.popleft()
        print(cur, end=' ')
        for next in range(1,N+1):
            if not visited2[next] and graph[cur][next]:
                visited2[next]=True
                q.append(next)

N,M,V= map(int,read().split())

graph=[[False]*(N+1) for _ in range(N+1)]
visited=[False]*(N+1)
visited2=[False]*(N+1)

for _ in range(M):
    a,b=map(int,read().split())
    graph[a][b]=True
    graph[b][a]=True

#dfs : 재귀로 이용
dfs(V)
print()

#bfs : deque 큐 이용
q=deque([V])
visited2[V]=True
bfs()