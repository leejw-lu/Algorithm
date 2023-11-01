import sys
from collections import deque
read=sys.stdin.readline

#상하좌우 + 대각선 추가
dirX=[-1,1,0,0,-1,1,-1,1]
dirY=[0,0,-1,1,1,1,-1,-1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    graph[x][y]=0

    while q:
        x,y=q.popleft()
        for i in range(8):
            newX=x+dirX[i]
            newY=y+dirY[i]
            if newX < 0 or newX >= H or newY < 0 or newY >= W:
                continue
            if graph[newX][newY]==1:
                graph[newX][newY]=0
                q.append((newX,newY))

while True:
    W,H=map(int,read().split()) #너비W=>j 높이H=>i

    if W==0 and H==0:
        break

    graph=[]
    for _ in range(H):
        graph.append(list(map(int,read().split())))

    count=0 #섬의 개수
    for i in range(H):      #H=>i W=>j index 범위 주의!!
        for j in range(W):
            if graph[i][j]==1:
                bfs(i,j)
                count+=1
    print(count)
