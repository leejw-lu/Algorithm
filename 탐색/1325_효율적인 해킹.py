#pypy3으로 통과
import sys
from collections import deque
read=sys.stdin.readline

def bfs(idx):
    count=1
    q=deque([idx])
    visited=[False]*(N+1)
    visited[idx]=True

    while q:
        cur=q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next]=True
                q.append(next)
                count+=1
    return count
                

N,M=map(int,read().split())
graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[b].append(a) #단방향, 인접리스트

result=[]
for i in range(1,N+1):
    result.append(bfs(i))

maxC=max(result)
for i in range(len(result)):
    if maxC==result[i]:
        print(i+1, end=' ')
