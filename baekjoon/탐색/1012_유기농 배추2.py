import sys
from collections import deque
read=sys.stdin.readline
MAX=50+10

T= int(read())

dirX=[1,-1,0,0]
dirY=[0,0,1,-1]

def bfs(x,y):
    global graph, q
    while q:
        x, y=q.popleft()
        for i in range(4):
            newX=x+dirX[i]
            newY=y+dirY[i]
            if graph[newX][newY]:
                graph[newX][newY]=False
                q.append((newX,newY))
            
#graph
for _ in range(T):

    N,M,K=map(int,read().split())
    graph=[[False]*MAX for _ in range(MAX)]
    for _ in range(K):
        x,y=map(int, read().split())
        graph[x+1][y+1]=True

    count=0
    q=deque()
    for i in range(1,N+1):
        for j in range(1,M+1):
            if graph[i][j]:
                q.append((i,j))
                graph[i][j]=False
                bfs(i,j)
                count+=1

    #출력
    print(count)


