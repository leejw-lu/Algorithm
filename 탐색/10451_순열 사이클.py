import sys
sys.setrecursionlimit(10000)
read=sys.stdin.readline

def dfs(idx):
    global visited
    visited[idx]=True
    next=graph[idx]
    if not visited[next]:
        dfs(next)

T=int(read())
for _ in range(T):
    count=0  #순열 사이클 개수

    N=int(read())
    graph=[0] + list(map(int, read().split()))
    visited=[False]*(N+1)

    for i in range(1,N+1):
        if not visited[i]:
            dfs(i)
            count+=1
    print(count)