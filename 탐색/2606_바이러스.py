import sys
sys.setrecursionlimit(10000)
read=sys.stdin.readline

def dfs(idx):
    global visited, count
    visited[idx]=True
    for next in range(1,N+1):
        if not visited[next] and graph[idx][next]:
            #print("11행의 dfs next:",next) # 노드1과 연결된 노드 모두 dfs탐색
            count+=1
            dfs(next)

N=int(read())
M=int(read())
graph=[[False]* (N+1) for _ in range(N+1)]
visited=[False] * (N+1)

for _ in range(M):
    a,b=map(int,read().split())
    graph[a][b]=True
    graph[b][a]=True

#for i in range(1,N+1):
 #   if not visited[i]:
  #      print("26행의 dfs 호출",i)
   #     dfs(i)

count=0
dfs(1)
print(count)
