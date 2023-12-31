import sys
from collections import deque
read=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y,0))

    while q:
        x,y,w=q.popleft()
        #visited[x][y] 방문했다고 continue하면 X. (벽 안지난, 벽 지난 case 나눠야.)
        if (x,y) == (n-1,m-1):
            return visited[x][y][w]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: 
                continue
            if graph[nx][ny]==1 and w==0: #다음 이동할 곳이 벽 and 벽 아직 안부쉈을 경우
                q.append((nx,ny,1))
                visited[nx][ny][1]=visited[x][y][0]+1
            elif graph[nx][ny]==0 and not visited[nx][ny][w]:
                q.append((nx,ny,w))
                visited[nx][ny][w]=visited[x][y][w]+1
    return -1

#입력
n,m= map(int,read().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,read().rstrip())))

#3차원 방문 표시 => [0, 0] : 벽 지나지 않은 경우, 벽을 지나온 경우
visited=[[[0,0] for _ in range(m)] for _ in range(n)]
visited[0][0][0]=1     #비용

print(bfs(0,0))