import sys
sys.setrecursionlimit(10 ** 9)
read=sys.stdin.readline

def dfs(idx):
    for next in graph[idx]:
        if not visited[next]:
            visited[next]=idx
            dfs(next)

N=int(read())
graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)

for _ in range(N-1):
    a,b=map(int,read().split()) # [[1,2], [2,3] .....]
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2,N+1):
    print(visited[i])