import sys
sys.setrecursionlimit(100000)
read=sys.stdin.readline

def dfs(idx,count):
    global visited,total
    visited[idx]=True
    #print("idx:",idx, "count촌수:", count)
    
    if idx==B:
        total=count
        return total

    for next in range(1,N+1):
        if not visited[next] and graph[idx][next]:
            dfs(next,count+1)

N=int(read())
A,B= map(int,read().split())
M=int(read())

graph=[[False]*(N+1) for _ in range(N+1)]
visited=[False]*(N+1)

for _ in range(M):
    x,y=map(int,read().split())
    graph[x][y]=True
    graph[y][x]=True

total=-1
dfs(A,0)
print(total)