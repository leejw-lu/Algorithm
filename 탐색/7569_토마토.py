import sys
from collections import deque
read=sys.stdin.readline

dirZ=[0,0,0,0,-1,1]
dirX=[-1,1,0,0,0,0]
dirY=[0,0,-1,1,0,0]

def bfs():
    while q:
        z,x,y=q.popleft()
        for i in range(6):
            newZ=z+dirZ[i]
            newX=x+dirX[i]
            newY=y+dirY[i]
            if newZ<0 or newZ>=H or newX<0 or newX>=N or newY<0 or newY>=M:
                continue
            if graph[newZ][newX][newY]==0:
                graph[newZ][newX][newY]=graph[z][x][y]+1
                q.append((newZ,newX,newY))

M,N,H=map(int,read().split())
graph=[[list(map(int,read().split())) for _ in range(N)] for _ in range(H)] #3차원 리스트

#토마토 1 찾아서 append
q=deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j]==1:
                q.append((k,i,j))

#토마토 검사
day=0
bfs()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j]==0: #안익은 토마토
                print(-1)
                exit(0)
            day=max(day, graph[k][i][j])

print(day-1)