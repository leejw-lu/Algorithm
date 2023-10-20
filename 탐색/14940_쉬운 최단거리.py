import sys
from collections import deque
read=sys.stdin.readline

dirX=[-1,1,0,0]
dirY=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=True

    while q:
        x,y=q.popleft()
        for i in range(4):
            newX=x+dirX[i]
            newY=y+dirY[i]
            if newX<0 or newX>=N or newY<0 or newY>=M:
                continue
            if not visited[newX][newY] and graph[newX][newY]==1:
                visited[newX][newY]=True
                result[newX][newY]=result[x][y]+1
                q.append((newX,newY))
                
N,M=map(int,read().split())
graph=[]
visited=[[False]*M for _ in range(N)]
result=[[-1]*M for _ in range(N)]

for i in range(N):
    graph.append(list(map(int,read().split())))

for i in range(N):
    for j in range(M):
        #목표 지점
        if graph[i][j]==2:
            result[i][j]=0
            bfs(i,j)
            
        #원래 못가는 땅
        if graph[i][j]==0:
            result[i][j]=0

#출력
for i in range(N):
    for j in range(M):
        print(result[i][j], end=' ')
    print()