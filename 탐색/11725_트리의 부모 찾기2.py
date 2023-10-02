import sys
from collections import deque
read=sys.stdin.readline

#부모노드 담을 배열-> visited배열 대신 사용하면 속도 빨라진다.

def bfs():
    q=deque()
    q.append(1)
    #visited[1]=True

    while q:
        cur=q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next]=cur #부모노드 추가
                #visited[next]=True
                q.append(next)                            

N=int(read())
graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
#result=[0]*(N+1) #부모 노드 담을 배열

for _ in range(N-1):
    a,b=map(int,read().split()) # [[1,2], [2,3] .....]
    graph[a].append(b)
    graph[b].append(a)

bfs()

for i in range(2,N+1):
    print(visited[i])