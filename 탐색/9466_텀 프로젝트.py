import sys
sys.setrecursionlimit(10 ** 6)
read=sys.stdin.readline

def dfs(idx):
    global result
    cycle.append(idx)
    visited[idx]=True
    next=graph[idx]

    if not visited[next]:
        dfs(next)
    else:
        if next in cycle: #사이클 탐색
            result+=cycle[cycle.index(next):]

T=int(read())
for _ in range(T):
    N=int(read())
    graph=[0]+list(map(int,read().split()))
    visited=[False]*(N+1)
    result=[]

    for i in range(1,N+1):
        if not visited[i]:
            cycle=[]
            dfs(i)

    print(N-len(result))