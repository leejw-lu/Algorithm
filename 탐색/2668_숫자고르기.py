import sys
sys.setrecursionlimit(10**6)
read=sys.stdin.readline

def dfs(idx):
    tmp.append(idx)
    visited[idx]=True
    next=graph[idx]

    if not visited[next]:
        dfs(next)
    else:
        if next in tmp:
            first=tmp.index(next)
            for s in tmp[first:] :
                result.append(s)

N=int(read())
graph=[0]+[int(read()) for _ in range(N)]
visited=[False]*(N+1)
result=[]

for i in range(1,N+1):
    if not visited[i]:
        tmp=[]
        dfs(i)

result.sort()
print(len(result))
for i in result:
    print(i)
