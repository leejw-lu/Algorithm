import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정 : BFS로 풀면 RecursionError 에러남
read=sys.stdin.readline
MAX= 50+ 10

dirX=[1,-1,0,0]
dirY=[0,0,1,-1]

def dfs(x,y):
    global graph, visited
    visited[x][y]=True
    for i in range(4):
        newX=x+dirX[i]
        newY=y+dirY[i]
        if graph[newX][newY] and not visited[newX][newY]:
            dfs(newX,newY)


T=int(read())
for _ in range(T):

    N, M, K= map(int,read().split())

    #graph
    graph=[[False]*(MAX) for _ in range(MAX)]
    visited=[[False]*(MAX) for _ in range(MAX)]

    #graph 정보
    for _ in range(K):
        x,y=map(int,read().split())
        graph[x+1][y+1]=True

    #아직 방문안한 지점 dfs
    count=0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if graph[i][j] and not visited[i][j]:
                dfs(i,j)
                count +=1

    print(count)