import sys
from collections import deque
read=sys.stdin.readline

dirX=[-1,1,0,0]
dirY=[0,0,-1,1]

def bfs():
    while q:
        x,y=q.popleft()
        for i in range(4):
            newX=x+dirX[i]
            newY=y+dirY[i]
            if newX<0 or newX>=N or newY<0 or newY>=M:
                continue
            if graph[newX][newY]==0:
                graph[newX][newY]=graph[x][y]+1
                q.append((newX,newY))   #연쇄니까 append

#입력
M,N=map(int,read().split())
graph=[]

for _ in range(N):
    graph.append(list(map(int,read().split())))

#1인 토마토 찾아 append
q=deque()
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            q.append((i,j))

#토마토 검사
result=0
bfs()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0: #안익은 토마토
            print(-1)
            exit(0)
        result = max(result, graph[i][j])

print(result-1) #처음에 1로 시작했으니 빼주기