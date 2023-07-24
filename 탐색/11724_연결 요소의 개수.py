#38424KB	556ms
import sys
sys.setrecursionlimit(10000)
read=sys.stdin.readline

def dfs(idx):
    visited[idx]=True
    for next in range(1,N+1):  
        if not visited[next] and graph[idx][next]:
            dfs(next)

N,M=map(int, read().split())
graph=[[False]*(N+1) for _ in range(N+1)]
visited=[False]*(N+1)

for _ in range(M):
    u, v = map(int, read().split())
    graph[u][v]=True
    graph[v][u]=True

count=0 #연결요소 개수
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        count+=1
print(count)