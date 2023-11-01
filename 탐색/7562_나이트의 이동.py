import sys
from collections import deque
read=sys.stdin.readline

dirX=[-2,-1,1,2,-2,-1,1,2]
dirY=[1,2,2,1,-1,-2,-2,-1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    
    while q:
        x,y=q.popleft()
        
        if x == d_x and y == d_y: #나이트 출발지==도착지
            return graph[x][y]

        for i in range(8):
            newX=x+dirX[i]
            newY=y+dirY[i]
            if 0 <= newX < L and 0 <= newY < L:
                if graph[newX][newY]==0:
                    graph[newX][newY]= graph[x][y]+1
                    q.append((newX,newY))

T=int(read())
for _ in range(T):
    L=int(read())
    graph=[[0]*L for _ in range(L)]
    s_x,s_y=map(int,read().split()) #출발지
    d_x,d_y=map(int,read().split())  #도착지
    print(bfs(s_x,s_y))


