import sys
from collections import deque
read=sys.stdin.readline

dirX=[-1,1,0,0]
dirY=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))

    while q:
        x,y=q.popleft()
        for i in range(4):
            newX=x+dirX[i]
            newY=y+dirY[i]
            if 0 <= newX < N and 0 <= newY < M:
                if graph[newX][newY]==1: #==1을 반드시 해줘야 한다.
                    graph[newX][newY]= graph[x][y]+1
                    q.append((newX,newY))

N,M=map(int, read().split())
graph=[]

for _ in range(N):
    graph.append(list(map(int,read().rstrip())))

bfs(0,0)
print(graph[N-1][M-1])