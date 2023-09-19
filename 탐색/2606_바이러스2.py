import sys
from collections import deque
read=sys.stdin.readline

def bfs():
    global count
    while q:
        cur=q.popleft()
        for next in range(1,N+1):
            if not visited[next] and graph[cur][next]:
                visited[next]=True
                q.append(next)
                count+=1


N=int(read())
M=int(read())

graph=[[False]*(N+1) for _ in range(N+1)]
visited=[False]*(N+1)

for _ in range(M):
    a,b=map(int,read().split())
    graph[a][b]=True
    graph[b][a]=True

count=0
q=deque([1])
visited[1]=True
bfs()

print(count)