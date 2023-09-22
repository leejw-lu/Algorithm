#BFS 풀이
import sys
from collections import deque
read=sys.stdin.readline

dirX=[-1,1,0,0]
dirY=[0,0,-1,1]

def bfs(x,y):
    global result,count
    count=1
    q=deque()
    q.append((x,y))
    graph[x][y]=False #visited 배열 안쓰려면-> 다시 방문 안하도록 False로 바꾸기.

    while q:
        x,y=q.popleft()
        
        for i in range(4):
            newX=x+dirX[i]
            newY=y+dirY[i]
            if newX < 0 or newX >= N or newY < 0 or newY >= N:
                continue
            if graph[newX][newY]:
                graph[newX][newY]=False #방문했던 곳 다시 False로.
                q.append((newX, newY))
                count+=1

    result.append(count)


N=int(read())
graph=[]
#visited=[[False]*(N+1) for _ in range(N+1)]

#입력
for _ in range(N):
    graph.append(list(map(int, read().rstrip())))

count=0
result=[]

for i in range(N):
    for j in range(N):
        if graph[i][j]:
            bfs(i,j)

print(len(result)) #총 단지 수
result.sort()
for i in result:
    print(i) #각 단지 개수



